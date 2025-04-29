import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris = load_iris()

dataframe = pd.DataFrame(iris.data, columns=iris.feature_names)
dataframe['target'] = iris.target

dataframe_seve=dataframe[dataframe["target"].isin([0, 1])]
dataframe_vevi=dataframe[dataframe["target"].isin([1, 2])]

seve_x = dataframe_seve.drop('target', axis=1)
seve_y = dataframe_seve["target"]

vevi_x = dataframe_vevi.drop('target', axis=1)
vevi_y = dataframe_vevi["target"]

seve_x_train, seve_x_test, seve_y_train, seve_y_test = train_test_split(seve_x, seve_y, test_size=0.3)
vevi_x_train, vevi_x_test, vevi_y_train, vevi_y_test = train_test_split(vevi_x, vevi_y, test_size=0.3)

clf_seve = LogisticRegression(random_state=0)
clf_seve.fit(seve_x_train, seve_y_train)

clf_vevi = LogisticRegression(random_state=0)
clf_vevi.fit(vevi_x_train, vevi_y_train)

seve_y_pred = clf_seve.predict(seve_x_test)
seve_accuracy = clf_seve.score(seve_x_test, seve_y_test)
print(f"Setosa-versicolor accuracy: {seve_accuracy:.2f}")

vevi_y_pred = clf_vevi.predict(vevi_x_test)
vevi_accuracy = clf_vevi.score(vevi_x_test, vevi_y_test)
print(f"Versicolor-virginica accuracy: {vevi_accuracy:.2f}")