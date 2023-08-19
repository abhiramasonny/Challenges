import numpy as np

def linear_regression(X, y):
    X = np.hstack((np.ones((X.shape[0], 1)), X))
    theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
    return theta

# Example usage
X = np.array([[1], [2], [3]])
y = np.array([2, 4, 5])
theta = linear_regression(X, y)
print("Linear Regression Coefficients:", theta)
