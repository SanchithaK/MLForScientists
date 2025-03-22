from mls.dataset.dataloader import load_dataset
from mls.dataset.feature_selection import select_best_features
from mls.train.trainer import train_model
from mls.evaluation.metrics import evaluate
import argparse


def run_workflow():
    dataset = load_dataset()
    best_features = select_best_features()
    # params = pyyaml.load("")
    
    trained_model = train_model(params={},data={})
    metric = evaluate(model=trained,params={},data={})
    return trained_model,metric

if __name__ == '__main__':

    run_workflow()
    parser = argparse.ArgumentParser(description='Train various models')
    parser.add_argument('--data_dir', type=str, required=True, help='Path to your data directory')
    

   
