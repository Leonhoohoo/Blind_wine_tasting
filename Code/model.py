
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.metrics import accuracy_score
import xgboost as xgb
from model_param_space import *



def objective(param_dict):
    param_dict = param_space_clf_xgb_tree
    print(param_dict)
    
    
    
if __name__ == "__main__":
    objective()
