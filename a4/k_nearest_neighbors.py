# k_nearest_neighbors.py: Machine learning implementation of a K-Nearest Neighbors classifier from scratch.
#
# Submitted by: Laya Harwin -- lharwin
#
# Based on skeleton code by CSCI-B 551 Fall 2022 Course Staff

import numpy as np
from utils import euclidean_distance, manhattan_distance


class KNearestNeighbors:
    """
    A class representing the machine learning implementation of a K-Nearest Neighbors classifier from scratch.

    Attributes:
        n_neighbors
            An integer representing the number of neighbors a sample is compared with when predicting target class
            values.

        weights
            A string representing the weight function used when predicting target class values. The possible options are
            {'uniform', 'distance'}.

        _X
            A numpy array of shape (n_samples, n_features) representing the input data used when fitting the model and
            predicting target class values.

        _y
            A numpy array of shape (n_samples,) representing the true class values for each sample in the input data
            used when fitting the model and predicting target class values.

        _distance
            An attribute representing which distance metric is used to calculate distances between samples. This is set
            when creating the object to either the euclidean_distance or manhattan_distance functions defined in
            utils.py based on what argument is passed into the metric parameter of the class.

    Methods:
        fit(X, y)
            Fits the model to the provided data matrix X and targets y.

        predict(X)
            Predicts class target values for the given test data matrix X using the fitted classifier model.
    """

    def __init__(self, n_neighbors = 5, weights = 'uniform', metric = 'l2'):
        # Check if the provided arguments are valid
        if weights not in ['uniform', 'distance'] or metric not in ['l1', 'l2'] or not isinstance(n_neighbors, int):
            raise ValueError('The provided class parameter arguments are not recognized.')

        # Define and setup the attributes for the KNearestNeighbors model object
        self.n_neighbors = n_neighbors
        self.weights = weights
        self._X = None
        self._y = None
        self._distance = euclidean_distance if metric == 'l2' else manhattan_distance

    def fit(self, X, y):
        """
        Fits the model to the provided data matrix X and targets y.

        Args:
            X: A numpy array of shape (n_samples, n_features) representing the input data.
            y: A numpy array of shape (n_samples,) representing the true class values for each sample in the input data.

        Returns:
            None.
        """
        # Assigning train input data and class values 
        self._X = X
        self._Y = y
        return None
        #raise NotImplementedError('This function must be implemented by the student.')

    def predict(self, X):
        """
        Predicts class target values for the given test data matrix X using the fitted classifier model.

        Args:
            X: A numpy array of shape (n_samples, n_features) representing the test data.

        Returns:
            A numpy array of shape (n_samples,) representing the predicted target class values for the given test data.
        """
        # Calculating distance between test and train samples
        distance = np.zeros((X.shape[0], self._X.shape[0]), dtype=float)
        for i in range(X.shape[0]):
          for j in range(self._X.shape[0]):
            distance[i][j] = self._distance(X[i], self._X[j])

        # Initializing neighbors, Y_prediction and neighbors_distance 
        neighbors = np.zeros((X.shape[0], self.n_neighbors), dtype= int)
        Y_prediction = np.zeros(X.shape[0], dtype = int)
        neighbors_distance = np.zeros((X.shape[0], self.n_neighbors), dtype= float)

        # Finding k nearest neighbour for each test sample and their distances
        for i in range(X.shape[0]):
          indexes = np.argsort(distance[i])
          neighbors[i] = self._Y[indexes[0:self.n_neighbors]]
          neighbors_distance[i] = np.sort(distance[i])[0:self.n_neighbors]

        # If the weight is uniform, we do majority voting
        if self.weights == 'uniform':
          for j in range(X.shape[0]):
            temp = np.unique(neighbors[j], return_counts=True)
            Y_prediction[j] = temp[0][np.argmax(temp[1])]

        # If the weight is not uniform, we assign weights proportional to the inverse of the distance from the test sample to each neighbor.
        else:
          for j in range(X.shape[0]):
            a_dict = {}
            for i,n in enumerate(neighbors[j]):
              if n in a_dict:
                a_dict[n] += 1/(neighbors_distance[j][i] + 0.0000001)
              else:
                a_dict[n] = 1/(neighbors_distance[j][i] + 0.0000001)
            Y_prediction[j] = max(a_dict, key=a_dict.get)

        return Y_prediction




        #raise NotImplementedError('This function must be implemented by the student.')
