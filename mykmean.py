import numpy as np
from utils import sum_of_squares


class MyKMean:

    def __init__(self, n_centers, seed=0):
        self.seed = seed
        self.n_centers = n_centers
        self.labels = None
        self.centers = None

    def allocate_to_centers(self, X):
        n = X.shape[0]
        clusters = np.empty(n)
        for i, x_i in enumerate(X):
            clusters[i] = np.argmin(
                map(lambda x: sum_of_squares(x_i, x), self.centers)
                )
        return clusters

    def recalculate_centers(self, X):
        means = np.empty((self.n_centers, X.shape[1]))
        for i in xrange(self.n_centers):
            means[i] = np.mean(X[self.labels == i], axis=0)
        return means

    def fit(self, X):
        self.centers = X[np.random.choice(len(X), self.n_centers)]
        new_labels = self.allocate_to_centers(X)

        while np.all(self.labels != new_labels):
            self.labels = new_labels
            self.centers = self.recalculate_centers(X)
            new_labels = self.allocate_to_centers(X)
