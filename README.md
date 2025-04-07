
## Set up conda environment
Please install the env.yaml file depending on your Operating System 
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

