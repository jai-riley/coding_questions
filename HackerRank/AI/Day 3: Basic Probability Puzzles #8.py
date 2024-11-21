"""
Objective
In this challenge, we practice calculating probability.

Task
In a certain city, the probability of a resident not reading
the morning newspaper is 1/2, and the probability of a resident
not reading the evening newspaper is 2/5. The probability they
will read both newspapers is 1/5.

Find the probability that a resident reads a morning or evening newspaper.
"""
from fractions import Fraction

prob_morning = 1 - Fraction(1, 2)
prob_evening = 1 - Fraction(2, 5)
prob_both = Fraction(1, 5)

print(prob_morning+prob_evening-prob_both)

