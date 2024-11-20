"""
Objective
In this challenge, we practice calculating probability.

Task
There are 10 people about to sit down around a round table.
Find the probability that 2 particular people will sit next
to one another.
"""
from fractions import Fraction

indices = [i for i in range(10)]
total = 0
combinations = []

for one in indices:
    for two in indices[0:one] + indices[one + 1:]:
        if one == 0:
            if two == 9 or two == 1:
                combinations.append([one, two])
        elif one == 9:
            if two == 0 or two == 8:
                combinations.append([one, two])
        else:
            if one == (two - 1) or one == (two + 1):
                combinations.append([one, two])
        total += 1

print(Fraction(len(combinations), total))
