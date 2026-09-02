# Last updated: 9/2/2026, 9:13:54 AM
1class Solution(object):
2    def isHappy(self, n):
3        """
4        :type n: int
5        :rtype: bool
6        """
7        seen = set()
8        while n!=1:
9            if n in seen:
10                return False
11            seen.add(n)
12            tot = 0
13            while n > 0:
14                digit = n%10
15                tot += digit* digit
16                n//=10
17            n = tot
18        return True
19        