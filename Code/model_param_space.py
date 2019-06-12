import numpy as np
from hyperopt import hp

from config import *

## xgboost
xgb_random_seed = RANDOM_SEED
xgb_n_estimators_min = 100
xgb_n_estimators_max = 1000
xgb_n_estimators_step = 10

## classification with tree booster
param_space_clf_xgb_tree = {
    "booster": "gbtree",
    "objective": "multi:softprob",
    "n_estimators" : hp.quniform("n_estimators", xgb_n_estimators_min, xgb_n_estimators_max, xgb_n_estimators_step),
    "learning_rate" : hp.qloguniform("learning_rate", np.log(0.002), np.log(0.1), 0.002),
    "gamma": hp.loguniform("gamma", np.log(1e-10), np.log(1e1)),
    "reg_alpha" : hp.loguniform("reg_alpha", np.log(1e-10), np.log(1e1)),
    "reg_lambda" : hp.loguniform("reg_lambda", np.log(1e-10), np.log(1e1)),
    "min_child_weight": hp.loguniform("min_child_weight", np.log(1e-10), np.log(1e2)),
    "max_depth": hp.quniform("max_depth", 1, 10, 1),
    "subsample": hp.quniform("subsample", 0.1, 1, 0.05),
    "colsample_bytree": 1,
    "colsample_bylevel": hp.quniform("colsample_bylevel", 0.1, 1, 0.05),
    "n_jobs": -1,
    "seed": xgb_random_seed,
}
