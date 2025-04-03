from mls.dataset.dataloader import load_dataset
from mls.dataset.feature_selection import select_best_features
from mls.train.trainer import train_model
from mls.evaluation.metrics import evaluate
from mls.utils.utils import load_yaml
from pathlib import Path
import os
# import argparse

import yaml


def run_workflow():
    params_path = os.path.join(Path(__file__).parent,"mls","config","mls.yaml")
    print(params_path)
    params = load_yaml(params_path)
    print("###params###")
    print(params)
    train_dataset = load_dataset(params=params['dataset'],split="train")
    test_dataset = load_dataset(params=params['dataset'],split="test")
    trained_model = train_model(params=params['model'],data=train_dataset)
    metric = evaluate(model=trained,params=params['model'],data=test_dataset)
    return trained_model,metric

if __name__ == '__main__':

    trained_model,metric = run_workflow()
  
   
