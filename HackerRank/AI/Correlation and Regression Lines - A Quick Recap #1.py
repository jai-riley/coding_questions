"""
Here are the test scores of 10 students in physics and history:

Physics Scores  15  12  8   8   7   7   7   6   5   3
History Scores  10  25  17  11  13  17  20  13  9   15
Compute Karl Pearson’s coefficient of correlation between these scores.
Compute the answer correct to three decimal places.
"""

p = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
h = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
mean_p = sum(p) / len(p)
mean_h = sum(h) / len(h)
numerator = sum([(p[x]-mean_p)*(h[x]-mean_h) for x in range(len(p))])
squared_sum_p = sum([(p[x]-mean_p)**2 for x in range(len(p))])
squared_sum_h = sum([(h[x]-mean_h)**2 for x in range(len(h))])
denominator = ((squared_sum_p)**0.5) * ((squared_sum_h)**0.5)
print(f"{(numerator/denominator):.3f}")
