import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris, make_classification

class_x, class_y = make_classification(n_samples=1000, 
                           n_features=2, 
                           n_redundant=0, 
                           n_informative=2,
                           random_state=1, 
                           n_clusters_per_class=1)

fig, ax = plt.subplots()

fig.set_size_inches(10, 6)
ax.set_title('Classification dataset')
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')

ax.scatter(class_x[:, 0], class_x[:, 1], c=class_y, cmap='Spectral')

class_x_train, class_x_test, class_y_train, class_y_test = train_test_split(class_x, 
                                                                            class_y, 
                                                                            test_size=0.3)
clf_class = LogisticRegression(random_state=0)
clf_class.fit(class_x_train, class_y_train)
class_accuracy = clf_class.score(class_x_test, class_y_test)
print(f'Accuracy for make_classification(): {class_accuracy:.2f}')

plt.show()