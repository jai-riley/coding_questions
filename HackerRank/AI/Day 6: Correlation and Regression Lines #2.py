"""
Objective
In this challenge, we practice calculating the slope of
regression lines.

Task
There are 2 series of data involving index numbers:
P for price index and S for the commodity stock.
The mean and standard deviation of P are 100 and 8, respectively.
The mean and standard deviation of S are 103 and 4, respectively.
The R^2 correlation coefficient between the two series is 0.4.

With this data, obtain the slope of the regression line of P on S,
correct to a scale of 2 decimal places.

https://gocardless.com/guides/posts/how-to-calculate-a-regression-line/#:~:text=To%20calculate%20slope%20for%20a,going%20downhill%20rather%20than%20upwards.
"""

# formula = stand_d_P/stand_d_S * correlation
stand_d_P = 8
stand_d_S = 4
R = 0.4 ** 0.5
print(f"{(stand_d_P / stand_d_S * R):.2f}")
