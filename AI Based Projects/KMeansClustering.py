import numpy as np

def kmeans(X, k, max_iters=100):
    centroids = X[np.random.choice(X.shape[0], k, replace=False)]
    
    for _ in range(max_iters):
        distances = np.sqrt(((X - centroids[:, np.newaxis])**2).sum(axis=2))
        labels = np.argmin(distances, axis=0)
        
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    
    return centroids, labels

X = np.array([[1, 2], [2, 3], [8, 7], [9, 8], [10, 9]])
k = 2
centroids, labels = kmeans(X, k)
print("Centroids:", centroids)
print("Labels:", labels)
