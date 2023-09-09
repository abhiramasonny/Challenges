import numpy as np
class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
    
    def fit(self, X, y, depth=0):
        if self.max_depth is not None and depth >= self.max_depth:
            return np.bincount(y).argmax()
        
        if np.all(y == y[0]):
            return y[0]
        
        feature, threshold = self.split(X, y)
        if feature is None:
            return np.bincount(y).argmax()
        
        left_indices = X[:, feature] < threshold
        right_indices = ~left_indices
        
        left_subtree = self.fit(X[left_indices], y[left_indices], depth + 1)
        right_subtree = self.fit(X[right_indices], y[right_indices], depth + 1)
        
        return (feature, threshold, left_subtree, right_subtree)
    
    def split(self, X, y):
        best_gini = float('inf')
        best_feature = None
        best_threshold = None
        
        for feature in range(X.shape[1]):
            values = np.sort(np.unique(X[:, feature]))
            for i in range(1, len(values)):
                threshold = (values[i - 1] + values[i]) / 2
                y_left = y[X[:, feature] < threshold]
                y_right = y[X[:, feature] >= threshold]
                gini = (len(y_left) / len(y)) * self.gini_impurity(y_left) + (len(y_right) / len(y)) * self.gini_impurity(y_right)
                
                if gini < best_gini:
                    best_gini = gini
                    best_feature = feature
                    best_threshold = threshold
        
        return best_feature, best_threshold
    
    def gini_impurity(self, y):
        _, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)
        return 1 - np.sum(probabilities ** 2)

# Example usage
X = np.array([[1, 2], [2, 3], [8, 7], [9, 8], [10, 9]])
y = np.array([0, 0, 1, 1, 1])
dt = DecisionTree()
tree = dt.fit(X, y)
print(tree)
