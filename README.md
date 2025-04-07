
## Set up conda environment
```
conda env create -f env_{OS}.yaml where OS is mac/windows
conda activate mls
pip install -e .
```
### Prefix
You can add a prefix identifier in env_{OS}.yaml to specify location to save enviornment in

## Train
Run a single model
```
python3 main.py
```

