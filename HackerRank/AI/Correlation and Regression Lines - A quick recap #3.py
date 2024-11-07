"""
Here are the test scores of 10 students in physics and history:

Physics Scores  15  12  8   8   7   7   7   6   5   3
History Scores  10  25  17  11  13  17  20  13  9   15
When a student scores 10 in Physics, what is his probable score in History?
Compute the answer correct to one decimal place.
"""
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([15, 12, 8, 8, 7, 7, 7, 6, 5, 3])
X = X.reshape(-1, 1)
Y = np.array([10, 25, 17, 11, 13, 17, 20, 13, 9, 15])
Y = Y.reshape(-1, 1)
tests = np.array([10])
tests = tests.reshape(1, -1)

model = LinearRegression()
model.fit(X, Y)
predictions = model.predict(tests)
for x in predictions:
    print(f"{x[0]:.1f}")

