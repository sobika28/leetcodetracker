# Last updated: 9/2/2026, 9:04:32 AM
1class Solution(object):
2    def grayCode(self, n):
3        """
4        :type n: int
5        :rtype: List[int]
6        """
7        ans =[]
8        for i in range(2**n):
9            ans.append(i^(i>>1))
10        return ans
11        