
## Set up conda environment
```
conda env create -f environment.yaml
conda activate mls
pip install -e .
```

## Train
Run a single model
```
python mls/main.py --data_dir <path> --model nn --lr 0.003
```

