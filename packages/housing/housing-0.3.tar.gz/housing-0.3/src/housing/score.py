"""Model Scoring."""

import argparse
import configparser
import logging
import pickle

import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error

parser = argparse.ArgumentParser()

parser.add_argument(
    "-d", "--data_path", help="Path for input datasets after processing",
)
parser.add_argument(
    "-m", "--model_path", help="enter the model pickle file path"
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


def load_housing_data_processed(data_path):
    """Read Housing data and return dataframe."""
    train_path = data_path + "/train_processed.csv"
    valid_path = data_path + "/test_processed.csv"
    logging.info("Reading processed data")
    return pd.read_csv(train_path), pd.read_csv(valid_path)


train_set, test_set = load_housing_data_processed(args.data_path)

logging.info("Loading model data from pickle files")
with open((args.model_path + "/linear_model.pkl"), "rb") as file:
    lin_reg = pickle.load(file)

with open((args.model_path + "/tree_model.pkl"), "rb") as file:
    tree_model = pickle.load(file)

with open((args.model_path + "/random_forest.pkl"), "rb") as file:
    random_forest = pickle.load(file)

X_train = train_set.drop("median_house_value", axis=1)
y_train = train_set["median_house_value"].copy()

X_test = test_set.drop("median_house_value", axis=1)
y_test = test_set["median_house_value"].copy()


def scoring(model, X_train, y_train, X_test, y_test):
    housing_predictions = model.predict(X_train)
    train_mse = mean_squared_error(y_train, housing_predictions)
    train_rmse = np.sqrt(train_mse)
    train_rmse

    train_mae = mean_absolute_error(y_train, housing_predictions)
    train_mae

    final_predictions = model.predict(X_test)
    final_mse = mean_squared_error(y_test, final_predictions)
    final_rmse = np.sqrt(final_mse)

    final_mae = mean_absolute_error(y_test, final_predictions)
    final_mae
    return train_rmse, train_mae, final_rmse, final_mae


logging.info("Testing Linear Regression")
lin_tr_rmse, lin_tr_mae, lin_te_rmse, lin_te_mae = scoring(
    lin_reg, X_train, y_train, X_test, y_test
)
logging.info(
    " Train RMSE = {}, Train MAE = {}".format(lin_tr_rmse, lin_tr_mae)
)
logging.info(" Test RMSE = {}, Test MAE = {}".format(lin_te_rmse, lin_te_mae))

logging.info("Testing Decision Tree Regression")
dt_tr_rmse, dt_tr_mae, dt_te_rmse, dt_te_mae = scoring(
    tree_model, X_train, y_train, X_test, y_test
)
logging.info(" Train RMSE = {}, Train MAE = {}".format(dt_tr_rmse, dt_tr_mae))
logging.info(" Test RMSE = {}, Test MAE = {}".format(dt_te_rmse, dt_te_mae))

logging.info("Testing Random Forest Regression")
rf_tr_rmse, rf_tr_mae, rf_te_rmse, rf_te_mae = scoring(
    random_forest, X_train, y_train, X_test, y_test
)
logging.info(" Train RMSE = {}, Train MAE = {}".format(rf_tr_rmse, rf_tr_mae))
logging.info(" Test RMSE = {}, Test MAE = {}".format(rf_te_rmse, rf_te_mae))

logging.info("Finished")
