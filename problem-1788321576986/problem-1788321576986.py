# Last updated: 9/2/2026, 9:29:36 AM
1class Solution:
2    def rob(self, nums):
3        prev2 = 0
4        prev1 = 0
5
6        for money in nums:
7            current = max(prev1, prev2 + money)
8
9            prev2 = prev1
10            prev1 = current
11
12        return prev1