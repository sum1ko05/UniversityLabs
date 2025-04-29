import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
dataframe = pd.DataFrame(iris.data, columns=iris.feature_names)
dataframe['target'] = iris.target

colors = {0: 'tab:purple', 1: 'green', 2: 'tab:olive'}
fig, ((plot_sepal), (plot_petal)) = plt.subplots(1, 2) 

def plot_stats(ax, name: str) -> None:
    ax.set_title(f'{name.capitalize()} stats')
    for target in np.unique(iris.target):
        ax.scatter(
            x=dataframe[dataframe['target'] == target][f'{name} length (cm)'],
            y=dataframe[dataframe['target'] == target][f'{name} width (cm)'],
            c=colors[target],
            label=iris.target_names[target]
        )
    ax.set_xlabel('Length (cm)')
    ax.set_ylabel('Width (cm)')
    ax.legend()

plot_stats(plot_sepal, 'sepal')
plot_stats(plot_petal, 'petal')
plt.show()