"""
Write a function to find the longest common prefix string amongst an array
of strings.

If there is no common prefix, return an empty string "".
"""


class Solution(object):
    def longestCommonPrefix(self, strs, num=0):
        """
        :param num: index of letter in strings to check
        :type strs: List[str]
        :rtype: str
        """

        if num >= len(min(strs, key=len)):
            return ""
        else:
            x = [s[num] == strs[0][num] for s in strs if s]
            if False not in x:
                return strs[0][num] + self.longestCommonPrefix(strs, num + 1)
            else:
                return ""
