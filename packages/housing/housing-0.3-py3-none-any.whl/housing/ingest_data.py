import argparse
import configparser
import logging
import os
import tarfile
from pathlib import Path

import numpy as np
import pandas as pd
from six.moves import urllib
from sklearn.model_selection import StratifiedShuffleSplit, train_test_split

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output_path", help="enter the output path")
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

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("..", "..", "data", "raw")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


fetch_housing_data()
housing = load_housing_data()


train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

housing["income_cat"] = pd.cut(
    housing["median_income"],
    bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
    labels=[1, 2, 3, 4, 5],
)


split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

filepath1 = Path(args.output_path + "/train.csv")
filepath2 = Path(args.output_path + "/test.csv")

filepath1.parent.mkdir(parents=True, exist_ok=True)
filepath2.parent.mkdir(parents=True, exist_ok=True)

# storing train and test datasets
strat_train_set.to_csv(path_or_buf=filepath1)
strat_test_set.to_csv(path_or_buf=filepath2)

logging.info("Training and test dataset created")
logging.info("Finished")
