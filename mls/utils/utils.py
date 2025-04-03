import yaml
import matplotlib.pyplot as plt
from pathlib import Path


def load_yaml(filepath = ""):
    with open(filepath, 'r') as file:
        params = yaml.safe_load(file)
    return params



def plot_and_save(x=[],y=[],plot_type ="line",title="",filename=""):
    if plot_type == "scatter":
        plt.scatter
    else:
        plt.plot(x,y)
    plt.title(title)
    
    output_folder = Path(__file__).parent.parent.parent
    filepath = os.path.join(output_folder,"plots",filename)
    plt.savefig(filepath)  
    plt.show()

