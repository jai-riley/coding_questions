"""
You are given an array of N integers separated by spaces, all in one line.

Display the following:

Mean (m): The average of all the integers.

Median of this array: In case, the number of integers is odd, the middle element;
else, the average of the middle two elements.

Mode: The element(s) which occurs most frequently.
If multiple elements satisfy this criteria, display the numerically smallest one.

Standard Deviation (SD).
SD = (((x1-m)2+(x2-m)2+(x3-m)2+(x4-m)2+...(xN-m)2))/N)0.5
where xi is the ith element of the array

Lower and Upper Boundary of the 95% Confidence Interval for the mean,
separated by a space. This might be a new term to some. However,
it is an important concept with a simple, formulaic solution. Look it up!

Other than the modal values (which should all be integers) the answers should
be in decimal form till one place of decimal (0.0 format).
An error margin of +/- 0.1 will be tolerated for the standard deviation and the
confidence interval boundaries. The mean, mode and median values should match
the expected answers exactly.
"""

num = int(input())
N = list(map(int, input().split()))
N.sort()

# Calculate mean
m = sum(N) / num
print(m)

# Calculate median
if num % 2 == 0:
    median = (N[(num // 2) - 1] + N[num // 2]) / 2
else:
    median = N[num // 2]
print(median)

# Calculate mode
from collections import Counter
count = Counter(N)
max_count = max(count.values())
modes = [k for k, v in count.items() if v == max_count]
print(min(modes))

# Calculate standard deviation
sd = (sum((x - m) ** 2 for x in N) / num) ** 0.5
print(f"{sd:.1f}")

# Calculate confidence interval for the mean
se = sd / (num ** 0.5) * 1.96
print(f"{(m - se):.1f} {(m + se):.1f}")
