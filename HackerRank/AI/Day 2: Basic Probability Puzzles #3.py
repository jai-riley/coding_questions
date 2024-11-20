"""
Objective
In this challenge, we practice calculating probability.

Task
There are 3 urns: X, Y and Z.

Urn X contains 4 red balls and 3 black balls.
Urn Y contains 5 red balls and 4 black balls.
Urn Z contains 4 red balls and 4 black balls.
One ball is drawn from each urn. What is the probability that the
3 balls drawn consist of 2 red balls and 1 black ball?
"""
from fractions import Fraction


def urns(a):
    prob = [Fraction(x[0], sum(x)) for x in a]
    prob_c = [1 - x for x in prob]
    n = len(a)
    ans = 0
    for i in range(n):
        p = prob_c[i] * prob[(i + 1) % n] * prob[(i + 2) % n]
        ans += p
    return ans


b = [[4, 3], [5, 4], [4, 4]]
print(urns(b))
