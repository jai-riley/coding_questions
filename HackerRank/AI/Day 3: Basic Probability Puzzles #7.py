"""
Objective
In this challenge, we practice calculating probability.

Task
A firm produces steel pipes in three plants.

Plant A produces 500 units per day and
has a fraction defective output of 0.005.
Plant B produces 1000 units per day and
has a fraction defective output of 0.008.
Plant C produces 2000 units per day and
has a fraction defective output of 0.010.
At random, a pipe is selected from the day’s total production
and it is found to be defective.
What is the probability that it came from plant A?
"""
from fractions import Fraction

pipes = [[500, Fraction(5, 1000)],
         [1000, Fraction(8, 1000)],
         [2000, Fraction(10, 1000)]]

total = sum([x[0] for x in pipes])
num_defective = [(x[0] * x[1]) for x in pipes]
probs = [num_defective[x] / total for x in range(len(pipes))]

# a = selecting defective
# b = from plant A
# prob(a) = prob selecting defective
prob_a = Fraction(sum(num_defective) / total)
# prob(b) = prob of selecting from plant A
prob_b = Fraction(pipes[0][0], total)
# prob(a|b) = prob of defective given you are selecting from plant A
prob_a_b = pipes[0][1]

# prob(b|a) = prob of plant A given it is defective
#           = (prob(a|b) * prob(b)) / prob(a)
print(Fraction(prob_a_b * prob_b, prob_a))
