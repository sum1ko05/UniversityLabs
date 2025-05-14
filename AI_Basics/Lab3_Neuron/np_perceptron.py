from enum import Enum
import warnings
import numpy as np

class Activation(Enum):
    Step = 0
    Sigmoid = 1
    ReLU = 2

class Perceptron:
    def __init__(self, random_init=True, max_iter=100, activation=Activation.Step):
        self.random_init = random_init
        self.max_iter = max_iter
        self.activation = activation
        self.weights = None
        self.bias = None
        self.errors_ = []

    def _init_weights(self, features_size):
        if self.random_init:
            self.weights = np.random.rand(features_size)
            self.bias = np.random.rand()
        else:
            self.weights = np.zeros(features_size)
            self.bias = 0.0

    def _activate(self, x):
        if self.activation == Activation.Step:
            return 1 if x >= 0 else 0
        elif self.activation == Activation.Sigmoid:
            return 1 / (1 + np.exp(-x))
        elif self.activation == Activation.ReLU:
            return max(0, x)
        
    def fit(self, X, Y):
        samples_size, features_size = X.shape
        self._init_weights(features_size)

        for i in range(self.max_iter):
            #print(f"Iteration: {i}")
            error = 0
            for Xi, target in zip(X, Y):
                linear_output = np.dot(Xi, self.weights) + self.bias
                prediction = self._activate(linear_output)
                update = (target - prediction)
                self.weights += update * Xi
                self.bias += update
                error += int(update != 0.0)
            self.errors_.append(error)
            if error == 0:
                break
        # If we reached this, there still was errors on training
        # warnings.warn("Warning: error didn't reach zero during fitting!", RuntimeWarning)

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        if self.activation == Activation.Step:
            return np.where(linear_output >= 0, 1, 0)
        elif self.activation == Activation.Sigmoid:
            return np.where(linear_output >= 0.5, 1, 0)
        elif self.activation == Activation.ReLU:
            return np.where(linear_output >= 0, 1, 0)