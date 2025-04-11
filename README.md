

## MacOSX users
Please install homebrew as follows: 
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Then install a package needed to run XGBoost
```
brew install libomp
```
## Set up conda environment
Please install the env.yaml file 
```
conda env create -f env.yaml
conda activate mls
pip install -e .
```

### Prefix
You can add a prefix identifier in env_{OS}.yaml to specify location to save enviornment in
## Train
Run a single model
```
conda activate mls
python3 main.py
```

