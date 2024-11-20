"""
Objective
In this challenge, we practice calculating probability.

Task
Bag1 contains 4 red balls and 5 black balls.
Bag2 contains 3 red balls and 7 black balls.

One ball is drawn from the bag1, and 2 balls are drawn from bag2.
Find the probability that 2 balls are black and 1 ball is red.
"""
from fractions import Fraction

b = [[4, 5], [3, 7]]
prob = [Fraction(x[0], sum(x)) for x in b]
prob_c = [1 - x for x in prob]
p = 0
p += prob[0] * prob_c[1] * (Fraction(b[1][1]-1, sum(b[1]) - 1))  # red black black
p += prob_c[0] * prob_c[1] * (Fraction(b[1][0], sum(b[1]) - 1))  # black black red
p += prob_c[0] * prob[1] * (Fraction(b[1][1], sum(b[1]) - 1))  # black red black
