import argparse
import configparser
import logging
import pickle

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor

parser = argparse.ArgumentParser()
parser.add_argument(
    "-i", "--input_path", help="enter the input path for train data"
)
parser.add_argument(
    "-o",
    "--output_path_pickle",
    help="enter the output path for storing pickle file",
)
parser.add_argument(
    "--log_level",
    help="enter log level like DEBUG",
    choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
)
parser.add_argument(
    "--log_path", help="enter the log file path with the file name"
)
parser.add_argument(
    "--console_log",
    type=int,
    help="write logs to console or not",
    choices=[0, 1],
)

args = parser.parse_args()

# setting default values from configuration file
config = configparser.ConfigParser()
config.read("default_config.conf")
defaults = {}
defaults.update(dict(config.items("Defaults")))
parser.set_defaults(**defaults)
args = parser.parse_args()

# setting log level, log path, console_log

numeric_level = getattr(logging, args.log_level.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError("Invalid log level: %s" % args.log_level)
logging.basicConfig(
    filename=args.log_path, filemode="w", level=numeric_level,
)

logging.info("Started")


def load_housing_dataset(input_data_path):
    logging.info("Reading train and test data")
    train_path = input_data_path + "/train.csv"
    test_path = input_data_path + "/test.csv"
    return pd.read_csv(train_path), pd.read_csv(test_path)


strat_train_set, strat_test_set = load_housing_dataset(args.input_path)

for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat", axis=1, inplace=True)

housing = strat_train_set.copy()

housing["rooms_per_household"] = housing["total_rooms"] / housing["households"]
housing["bedrooms_per_room"] = (
    housing["total_bedrooms"] / housing["total_rooms"]
)
housing["population_per_household"] = (
    housing["population"] / housing["households"]
)

housing = strat_train_set.drop(
    "median_house_value", axis=1
)  # drop labels for training set
housing_labels = strat_train_set["median_house_value"].copy()


imputer = SimpleImputer(strategy="median")

housing_num = housing.drop("ocean_proximity", axis=1)

logging.info("Pre-processing training data")

imputer.fit(housing_num)
X = imputer.transform(housing_num)

housing_tr = pd.DataFrame(X, columns=housing_num.columns, index=housing.index)
housing_tr["rooms_per_household"] = (
    housing_tr["total_rooms"] / housing_tr["households"]
)
housing_tr["bedrooms_per_room"] = (
    housing_tr["total_bedrooms"] / housing_tr["total_rooms"]
)
housing_tr["population_per_household"] = (
    housing_tr["population"] / housing_tr["households"]
)

housing_cat = housing[["ocean_proximity"]]
housing_prepared = housing_tr.join(
    pd.get_dummies(housing_cat, drop_first=True)
)

logging.info("Storing processed training data at {}".format(args.input_path))
housing_prep_processed = housing_prepared.copy()
housing_prep_processed["median_house_value"] = housing_labels
housing_prep_processed.to_csv(
    args.input_path + "/train_processed.csv", index=False
)

logging.info("Training linear regression")
lin_reg = LinearRegression()
lin_reg.fit(housing_prepared, housing_labels)


housing_predictions = lin_reg.predict(housing_prepared)

logging.info("Training decision tree")
tree_reg = DecisionTreeRegressor(random_state=42)
tree_reg.fit(housing_prepared, housing_labels)

housing_predictions = tree_reg.predict(housing_prepared)

logging.info("Training random forest")
param_grid = [
    # try 12 (3×4) combinations of hyperparameters
    {"n_estimators": [3, 10, 30], "max_features": [2, 4, 6, 8]},
    # then try 6 (2×3) combinations with bootstrap set as False
    {"bootstrap": [False], "n_estimators": [3, 10], "max_features": [2, 3, 4]},
]

forest_reg = RandomForestRegressor(random_state=42)
# train across 5 folds, that's a total of (12+6)*5=90 rounds of training
grid_search = GridSearchCV(
    forest_reg,
    param_grid,
    cv=5,
    scoring="neg_mean_squared_error",
    return_train_score=True,
)
grid_search.fit(housing_prepared, housing_labels)

final_model = grid_search.best_estimator_
final_model.fit(housing_prepared, housing_labels)

housing_predictions = final_model.predict(housing_prepared)

logging.info("Preparing test data")
X_test = strat_test_set.drop("median_house_value", axis=1)
y_test = strat_test_set["median_house_value"].copy()

X_test_num = X_test.drop("ocean_proximity", axis=1)
X_test_prepared = imputer.transform(X_test_num)
X_test_prepared = pd.DataFrame(
    X_test_prepared, columns=X_test_num.columns, index=X_test.index
)
X_test_prepared["rooms_per_household"] = (
    X_test_prepared["total_rooms"] / X_test_prepared["households"]
)
X_test_prepared["bedrooms_per_room"] = (
    X_test_prepared["total_bedrooms"] / X_test_prepared["total_rooms"]
)
X_test_prepared["population_per_household"] = (
    X_test_prepared["population"] / X_test_prepared["households"]
)

X_test_cat = X_test[["ocean_proximity"]]
X_test_prepared = X_test_prepared.join(
    pd.get_dummies(X_test_cat, drop_first=True)
)

logging.info("Storing processed test data at {}".format(args.input_path))
housing_prep_processed = X_test_prepared.copy()
housing_prep_processed["median_house_value"] = y_test
housing_prep_processed.to_csv(
    args.input_path + "/test_processed.csv", index=False
)

with open((args.output_path_pickle + "/linear_model.pkl"), "wb") as file:
    pickle.dump(lin_reg, file)
with open((args.output_path_pickle + "/tree_model.pkl"), "wb") as file:
    pickle.dump(tree_reg, file)
with open((args.output_path_pickle + "/random_forest.pkl"), "wb") as file:
    pickle.dump(grid_search, file)

logging.info("Saved model pickle at {}".format(args.output_path_pickle))

logging.info("Finished")
