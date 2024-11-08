"""
The Problem
Charlie wants to purchase office-space. He does a detailed survey of the
offices and corporate complexes in the area, and tries to quantify a lot
of factors, such as the distance of the offices from residential and other
commercial areas, schools and workplaces; the reputation of the construction
companies and builders involved in constructing the apartments; the distance
of the offices from highways, freeways and important roads; the facilities
around the office space and so on.

Each of these factors are quantified, normalized and mapped to values on a
scale of 0 to 1. Charlie then makes a table. Each row in the table corresponds
to Charlie's observations for a particular house. If Charlie has observed and
noted F features, the row contains F values separated by a single space, followed
by the office-space price in dollars/square-foot. If Charlie makes observations
for H houses, his observation table has (F+1) columns and H rows, and a total
of (F+1) * H entries.

Charlie does several such surveys and provides you with the tabulated data.
At the end of these tables are some rows which have just F columns (the price
per square foot is missing). Your task is to predict these prices. F can be
any integer number between 1 and 5, both inclusive.

There is one important observation which Charlie has made.

The prices per square foot, are (approximately) a polynomial function of the
features in the observation table. This polynomial always has an order less than 4

Input Format
The first line contains two space separated integers, F and N. Over here, F is
the number of observed features. N is the number of rows for which features
as well as price per square-foot have been noted.
This is followed by a table having F+1 columns and N rows with each row in
 a new line and each column separated by a single space. The last column
 is the price per square foot.

The table is immediately followed by integer T followed by T rows containing
F columns.
"""

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

