import numpy as np

def load_dataset(params={},split="train"):
    if params['random']:
        data = {'X':np.random.random((params['random_num_samples'],params['random_num_features'])),
        'y':np.random.random((params['random_num_samples'],params['random_num_target']))
        }
        return data
    else:
        if split == "train":
            pass
        elif split == "test":
            pass
        data = None
        return data