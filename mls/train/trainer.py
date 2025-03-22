from mls.models.neural import train_nn
def train_model(params={},data={}):
    if params['method'] == "nn":
        return train_nn(params=params,data=data)
    elif params["method"] == "xgboost":
        pass
    elif params["method"] == "kmeans":
        pass 


