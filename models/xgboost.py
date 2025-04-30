import xgboost as xgb

def train_xgboost(params={},data={}):
    model = xgb.XGBRegressor(objective=params['objective'], n_estimators=params['n_estimators'], learning_rate=params['lr'], max_depth=params['max_depth'])
    model.fit(data['X'], data['y'])
    return model
