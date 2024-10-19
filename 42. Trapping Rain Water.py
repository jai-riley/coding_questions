"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 0:
            return 0

        water = 0
        # left[i] will contain the height of the highest bar from the start to index i
        left = [0] * n
        left[0] = height[0]
        # right[i] with contain the height of the highest bar from the end to index i
        right = [0] * n
        right[n - 1] = height[n - 1]

        for x in range(1, n):
            left[x] = max(left[x - 1], height[x])

        for x in range(n - 2, -1, -1):
            right[x] = max(right[x + 1], height[x])

        for x in range(n):
            water += (min(left[x], right[x]) - height[x])
        return water

