"""
Here are the test scores of 10 students in physics and history:

Physics Scores  15  12  8   8   7   7   7   6   5   3
History Scores  10  25  17  11  13  17  20  13  9   15
When a student scores 10 in Physics, what is his probable score in History?
Compute the answer correct to one decimal place.
"""
p = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
h = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
X = 10
mean_p = sum(p) / len(p)
mean_h = sum(h) / len(h)
numerator = sum([(p[x]-mean_p)*(h[x]-mean_h) for x in range(len(p))])
squared_sum_p = sum([(p[x]-mean_p)**2 for x in range(len(p))])
w1 = numerator/squared_sum_p
w0 = mean_h - w1 * mean_p
y = w0 + w1 * X
print(y)
