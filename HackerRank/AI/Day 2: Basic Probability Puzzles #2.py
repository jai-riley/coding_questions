"""
Objective
In this challenge, we practice calculating probability.

Task
For a single toss of 2 fair (evenly-weighted) dice, find the probability that
the values rolled by each die will be different and their sum is 6.

Output Format

In the editor below, submit your answer as Plain Text in the form of an
irreducible fraction A/B, where A and B are both integers.
"""
count = 0
for one in range(1,6):
    for two in range(1,6):
        if (one + two) == 6 and one != two:
            count += 1

print(f"{count}/36")

