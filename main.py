from mls.dataset.dataloader import load_dataset
from mls.dataset.feature_selection import select_best_features
from mls.train.trainer import train_model
from mls.evaluation.metrics import evaluate
from mls.utils.utils import load_yaml
from pathlib import Path
import os

import yaml


def run_workflow():
    params_path = os.path.join(Path(__file__).parent,"mls","config","mls.yaml")
    print(params_path)
    params = load_yaml(params_path)
    print("###params###")
    print(params)
    dataset = load_dataset(params=params['dataset'])
    trained_model = train_model(params=params['model'],data=dataset['train'])
    metric = evaluate(model=trained_model,params=params['model'],data=dataset['test'])
    return trained_model,metric

if __name__ == '__main__':

    trained_model,metric = run_workflow()
  
   
