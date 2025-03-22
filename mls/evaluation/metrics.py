from sklearn.metrics import mean_absolute_error,r2_score
import torch

def evaluate(model=None,params = {},data={}):
    if params['model'] == 'nn':
        with torch.no_grad():
            y_pred = model(data['X'])
    if params['evaluation'] == 'mae':
        mae = mean_absolute_error(y_pred,data['y'])
        return mae
