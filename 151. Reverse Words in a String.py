"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters.
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated
by a single space.

Note that s may contain leading or trailing spaces or
multiple spaces between two words. The returned string should
only have a single space separating the words. Do not include any extra spaces.
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Remove any white space and make words in string indexable
        s = [x for x in s.strip().split(" ") if x != ""]
        new_s = [""] * len(s)
        for x in range(len(s)):
            new_s[x] = s[-(x + 1)]
        return " ".join(new_s)
