# Last updated: 9/1/2026, 9:31:32 PM
1class Solution:
2    def reverse(self, x):
3        sign = -1 if x < 0 else 1
4        
5        x = abs(x)
6        rev = int(str(x)[::-1])
7        
8        rev = rev * sign
9        
10        if rev < -2**31 or rev > 2**31 - 1:
11            return 0
12        
13        return rev