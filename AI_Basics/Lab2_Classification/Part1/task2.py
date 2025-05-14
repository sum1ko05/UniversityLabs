import pandas as pd
import seaborn
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
dataframe = pd.DataFrame(iris.data, columns=iris.feature_names)
dataframe['target'] = iris.target

seaborn.pairplot(dataframe, hue='target', palette='viridis')
plt.suptitle('Pairplot of Iris Dataset', y=1.00)
plt.show()