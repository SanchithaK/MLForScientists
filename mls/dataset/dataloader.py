import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
def load_dataset(params={}):
    if params['type']  == "random":
        data = {
        "train" :{'X':np.random.random((params['random_num_samples'],params['random_num_features'])),
        'y':np.random.random((params['random_num_samples'],params['random_num_target']))
        },
        "test":{'X':np.random.random((params['random_num_samples'],params['random_num_features'])),
        'y':np.random.random((params['random_num_samples'],params['random_num_target']))
        }
        }
        return data
    elif params["type"] == "singlecell":
        dataset_folder = os.path.join(params['folder'],params['type'])
        X = pd.read_csv(os.path.join(dataset_folder,"expression_matrix.csv"))
        y = pd.read_csv(os.path.join(dataset_folder,"labels.csv"))
        print("X.shape:",X.shape,"y.shape:",y.shape,y)
        le = LabelEncoder()
        le.fit(y.values.tolist())
        y = le.transform(y)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=params['test_size'], random_state=42)
        data = {
            "train" :{"X": X_train,"y":y_train},
            "test":{"X": X_test,"y":y_test}
        }
        return data 




