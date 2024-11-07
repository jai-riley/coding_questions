import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def linear_regression(X, Y):
    '''
    Solves linear regression using the closed form solution.
    Parameters:
    X (numpy array): Feature matrix of size (n, d+1), where n is the number of samples
                     and d is the number of features. The first column should be all 1s.
    Y (numpy array): Target vector of size (n, 1).

    Returns:
    predictor (function): A function that takes a feature vector and returns a predicted value.
    '''
    A = X.T @ X
    b = X.T @ Y
    w_hat = np.linalg.pinv(A) @ b
    def predictor(x):
        return x @ w_hat

    return predictor

F, N = map(int, input().split(" "))
X, Y = [], []
for _ in range(N):
    data = list(map(float, input().split()))
    X.append(data[:-1])
    Y.append(data[-1])

num_tests = int(input())
tests = [list(map(float, input().split())) for _ in range(num_tests)]

poly = PolynomialFeatures(degree=3)
X = poly.fit_transform(X)
tests = poly.fit_transform(tests)

# Below used the created linear regression function
model = linear_regression(X, Y)
predictions = model(tests)

# Below uses the sklearn linear regression
model = LinearRegression()
model.fit(X,Y)
predictions = model.predict(tests)
for x in predictions:
    print(f"{x:.2f}")

