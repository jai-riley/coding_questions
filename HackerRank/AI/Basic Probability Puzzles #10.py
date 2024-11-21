"""
Bill and Nina appear for an interview for two vacancies.
The probability of Bill’s selection is 1/3 and that of
Nina’s selection is 1/5. Find the probability that only
one of them will be selected.

Fill in the answer in the text box, in the form of an
irreducible fraction A/B where A and B are two integers.
"""
from fractions import Fraction

bill = Fraction(1, 3)
nina = Fraction(1, 5)
# prob(not bill)*prob(nina) + prob(not nina)*prob(bill)
prob_non = ((1 - bill) * nina) + ((1 - nina) * bill)
print(prob_non)
