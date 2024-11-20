"""
Objective
In this challenge, we practice calculating probability.

Task
Bag X contains 5 white balls and 4 black balls.
Bag Y contains 7 white balls and 6 black balls.
You draw 1 ball from bag X and, without observing its color,
put it into bag Y.
Now, if a ball is drawn from bag Y, find the probability that it is black.
"""
from fractions import Fraction

b = [[5, 4], [7, 6]]
p = 0
p += Fraction(b[0][0], sum(b[0]))*Fraction(b[1][1], sum(b[1])+1)  # white black
p += Fraction(b[0][1], sum(b[0]))*Fraction(b[1][1]+1, sum(b[1])+1)  # black black
print(p)
