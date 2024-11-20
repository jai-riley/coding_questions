"""
Objective
In this challenge, we practice calculating probability.

Task
In a single toss of 2 fair (evenly-weighted) 6-sided dice, find the probability of
that their sum will be at most 9.

Output Format
In the editor below, submit your answer as Plain Text in the form of an irreducible
fraction A/B, where A and B are both integers.

"""
count = 0
for one in range(4, 7):
    for two in range(4, 7):
        if (one == 4 and two > 5) or (one == 5 and two > 4) or (one == 6):
            count += 1

print(f"{36 - count}/36")
