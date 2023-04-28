import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import numpy as np
import sklearn.datasets as dt
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from scipy.stats import mode
from sklearn.metrics import confusion_matrix

class KMeansOnDigits():

    def __init__(self, n_clusters, random_state):
        self.n_clusters = n_clusters
        self.random_state = random_state

    def load_dataset(self):
        self.digits = dt.load_digits()

    def predict(self):
        model = KMeans(n_clusters=self.n_clusters, random_state=self.random_state)
        clusters = model.fit_predict(self.digits)
        self.clusters = clusters

    def get_labels(self):
        labels = np.zeros_like(self.clusters)
        for cluster in range(10):
            mask = (self.clusters == cluster)
            subarray = self.digits.target[mask]
            mode = np.bincount(subarray).argmax()
            labels[mask] = mode
        self.labels = labels
    
    def calc_accuracy(self):
        self.accuracy = round(accuracy_score(self.digits.target, self.labels), 2)

    def confusion_matrix(self):
        self.math = confusion_matrix(self.digits.target, self.labels)