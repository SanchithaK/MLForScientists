from sklearn.metrics import mean_absolute_error,r2_score
import torch

def evaluate(model=None,params = {},data={}):
    print(f"evaluate:params={params}")
    if params['method'] == 'nn':
        with torch.no_grad():
            y_pred = model(data['X'])
        mae = mean_absolute_error(y_pred,data['y'])
        print("mae:",mae)
        
    elif params['method'] == 'xgboost':
        y_pred = model.predict(data['X'])
        mae = mean_absolute_error(y_pred,data['y'])
        print("mae:",mae)
    
    return mae
