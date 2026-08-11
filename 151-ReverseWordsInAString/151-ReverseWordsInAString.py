# Last updated: 8/11/2026, 12:24:09 PM
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        return ' '.join(words[::-1])
        