"""
A candidate is selected for interview of management trainees for
3 companies. For the first company, there are 12 candidates, for
the second there are 15 candidates and for the third, there are
10 candidates.
Find the probability that he is selected in at
least one of the companies.
Assume that 1 candidate will be selected
in each of the interviews, and all candidates appearing for the
interview have an equal probability of getting selected.

Fill in the answer in the text box, in the form of an irreducible
fraction A/B where A and B are two integers.
"""
from fractions import Fraction

prob_1 = Fraction(1, 12)
prob_2 = Fraction(1, 15)
prob_3 = Fraction(1, 10)
# probability of not getting any of the jobs
prob_non = (1-prob_1)*(1-prob_2)*(1-prob_3)
print(1-prob_non)
