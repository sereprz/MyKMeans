class MyKMean:

    def __init__(self, n_centers, seed=0):
        self.n_centers = n_centers
        self.seed = seed

    def fit(X):
        # select k = n_centers of X as initial centres
        centers = X[np.random.choice(len(X), n_centers)]
        # allocate points to closest center
        clusters = allocate_to_centers(X, centers)
        # recalculate centers
        new_centers = recalculate_centers(X, clusters)
        # repeat until new centers = old centers

    def allocate_to_centers(X, centers):
        return clusters

    def recalculate_centers(X, labels):
        return new_centers
