import numpy as np
import pandas as pd
import seaborn as sns
from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix
import math

csv_path = "diabetes.csv"

class KNNClassifier:

    #Constuctor
    def __init__(self,k:int,test_split_ratio:float):
        self.k = k
        self.test_split_ratio = test_split_ratio
        self.x_train = None
        self.y_train = None
        self.x_test = None
        self.y_test = None
        self.y_preds = None

    @property
    def k_neighbors(self):
        return self.k
    
    @staticmethod 
    def load_csv(csv_path:str) ->Tuple[pd.DataFrame,pd.Series]:
        np.random.seed(42)
        dataset = pd.read_csv(csv_path, header=None)
        dataset = dataset.sample(frac=1, random_state=42).reset_index(drop=True)
        x,y = dataset.iloc[:,:4],dataset.iloc[:,-1]
        return x,y
    
    #Train test split try optim
    def train_test_split(self,features:pd.DataFrame,labels:pd.Series) -> None:
        test_size = int(len(features)*self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, 'Size mismatch!'

        self.x_train = features.iloc[:train_size,:]
        self.y_train = labels.iloc[:train_size]

        self.x_test = features.iloc[train_size:train_size+test_size,:]
        self.y_test = labels.iloc[train_size:train_size+test_size]

    def euclidean(self, element_of_x: pd.Series) -> pd.Series:
        return pd.Series((self.x_train - element_of_x).pow(2).sum(axis=1)).pow(1/2)

    def predict(self, x_test: pd.DataFrame) -> pd.Series:
        labels_pred = []
        for i, x_test_element in x_test.iterrows():
            distances = self.euclidean(x_test_element)
            distances = pd.DataFrame({'distance': distances, 'label': self.y_train})
            distances = distances.sort_values('distance')
            label_pred = mode(distances.iloc[:self.k,1])[0][0]
            labels_pred.append(label_pred)
        self.y_preds = pd.Series(labels_pred)

    def accuracy(self) -> float:
        true_positive = (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) * 100
    
    def confusion_matrix(self) -> np.ndarray:
        conf_matrix = pd.crosstab(self.y_test, self.y_preds)
        return conf_matrix

    def best_k(csv_path:str, test_split_ratio:float) -> Tuple[int,float]:
        best_k = 0
        best_acc = 0.0
        for k in range(1,21):
            knn = KNNClassifier(k=k,test_split_ratio=test_split_ratio)
            x,y = knn.load_csv(csv_path)
            knn.train_test_split(x,y)
            knn.predict(knn.x_test)
            acc = round(knn.accuracy(),2)
            if(acc > best_acc):
                best_k = k
                best_acc = acc
        return (best_k,best_acc)