

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
You can add a prefix identifier in env.yaml to specify location to save enviornment in
## Train
Run a single model
```
conda activate mls
python3 main.py
```

### Dataset
Reference:
```
Jessica E. Rexach, Yuyan Cheng, Lawrence Chen, Damon Polioudakis, Li-Chun Lin, Vivianne Mitri, Andrew Elkins, Xia Han, Mai Yamakawa, Anna Yin, Daniela Calini, Riki Kawaguchi, Jing Ou, Jerry Huang, Christopher Williams, John Robinson, Stephanie E. Gaus, Salvatore Spina, Edward B. Lee, Lea T. Grinberg, Harry Vinters, John Q. Trojanowski, William W. Seeley, Dheeraj Malhotra, Daniel H. Geschwind,
Cross-disorder and disease-specific pathways in dementia revealed by single-cell genomics,
Cell,
Volume 187, Issue 20,
2024,
Pages 5753-5774.e28,
ISSN 0092-8674,
https://doi.org/10.1016/j.cell.2024.08.019.
(https://www.sciencedirect.com/science/article/pii/S0092867424009103)
```

