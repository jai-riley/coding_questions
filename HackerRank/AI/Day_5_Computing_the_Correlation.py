"""
You are given the scores of N students in three different subjects - Mathematics,*Physics* and Chemistry; all of which have been graded on a scale of 0 to 100. Your task is to compute the Pearson product-moment correlation coefficient between the scores of different pairs of subjects (Mathematics and Physics, Physics and Chemistry, Mathematics and Chemistry) based on this data. This data is based on the records of the CBSE K-12 Examination - a national school leaving examination in India, for the year 2013.

Pearson product-moment correlation coefficient

This is a measure of linear correlation described well on this Wikipedia page:
https://en.wikipedia.org/wiki/Pearson_correlation_coefficient

Input Format

The first row contains an integer N.
This is followed by N rows containing three tab-space ('\t') separated integers, M P C corresponding to a candidate's scores in Mathematics, Physics and Chemistry respectively.
Each row corresponds to the scores attained by a unique candidate in these three subjects.

Input Constraints

1 <= N <= 5 x 105
0 <= M, P, C <= 100

Output Format

The output should contain three lines, with correlation coefficients computed
and rounded off correct to exactly 2 decimal places.
The first line should contain the correlation coefficient between Mathematics and Physics scores.
The second line should contain the correlation coefficient between Physics and Chemistry scores.
The third line should contain the correlation coefficient between Chemistry and Mathematics scores.
"""


def squared(n):
    return n ** 2


num = int(input())
math, physics, chem = zip(*(map(int, input().split("\t")) for _ in range(num)))

first = [math, physics, chem]
second = [physics, chem, math]
for x in range(3):
    f = first[x]
    s = second[x]
    sum_f = sum(f)
    sum_s = sum(s)
    squared_sum_f = sum(map(squared, f))
    squared_sum_s = sum(map(squared, s))
    sum_fs = sum([f[n] * s[n] for n in range(num)])
    numerator = (num * sum_fs) - (sum_f * sum_s)
    denominator = ((num * squared_sum_f - sum_f ** 2) ** 0.5) * ((num * squared_sum_s - sum_s ** 2) ** 0.5)
    print(f"{(numerator / denominator):.2f}")
