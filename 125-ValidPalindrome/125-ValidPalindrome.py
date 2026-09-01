# Last updated: 9/1/2026, 10:21:55 PM
1class Solution(object):
2    def isPalindrome(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7        s = s.lower()
8        n =""
9        for ch in s:
10           if ch.isalnum():
11               n+=ch
12        return n == n[::-1]