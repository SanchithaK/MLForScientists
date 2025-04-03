from mls.utils.utils import plot_and_save
from mls.models.neural import train_nn
from mls.models.xgboost import train_xgboost


def train_model(params={},data={}):
    if params['method'] == "nn":
        return train_nn(params=params[params['method'] ],data=data)
    elif params["method"] == "xgboost":
        return train_xgboost(params=params[params['method'] ],data=data)
    elif params["method"] == "kmeans":
        pass 


