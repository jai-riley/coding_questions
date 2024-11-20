"""
Here are the test scores of 10 students in physics and history:

Physics Scores  15  12  8   8   7   7   7   6   5   3
History Scores  10  25  17  11  13  17  20  13  9   15
Compute the slope of the line of regression obtained while treating
Physics as the independent variable. Compute the answer correct to
three decimal places.
"""

p = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
h = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
mean_p = sum(p) / len(p)
mean_h = sum(h) / len(h)
numerator = sum([(p[x]-mean_p)*(h[x]-mean_h) for x in range(len(p))])
squared_sum_p = sum([(p[x]-mean_p)**2 for x in range(len(p))])
print(f"{(numerator/squared_sum_p):.3f}")