import numpy as np
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        self.epochs = epochs
        self.lr = lr

    def fit(self, X: np.array, y: np.array):

        self.m = 0
        self.c = 0

        n = float(len(X)) 

        losses = []

        for i in range(self.epochs):
            self.y_pred = self.m * X + self.c

            residuals = self.y_pred - y
            loss = np.sum(residuals ** 2)
            losses.append(loss)
            D_m = (-2/n) * sum(X * residuals)
            D_c = (-2/n) * sum(residuals)  
            self.m = self.m + self.lr * D_m  
            self.c = self.c + self.lr * D_c  
            if i % 100 == 0:
                print(np.mean(y-self.y_pred))

    def predict(self, X):
        pred = []
        for x in X:
            y_pred = self.m*x + self.c
            pred.append(y_pred)
        print(pred)