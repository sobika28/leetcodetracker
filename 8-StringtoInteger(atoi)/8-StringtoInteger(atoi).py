# Last updated: 9/1/2026, 9:35:32 PM
1class Solution:
2    def myAtoi(self, s):
3        s = s.strip()
4
5        if not s:
6            return 0
7
8        sign = 1
9        i = 0
10
11        if s[0] == '-':
12            sign = -1
13            i += 1
14        elif s[0] == '+':
15            i += 1
16
17        num = 0
18
19        while i < len(s) and s[i].isdigit():
20            num = num * 10 + int(s[i])
21            i += 1
22        num = num * sign
23        if num < -2**31:
24            return -2**31
25        if num > 2**31 - 1:
26            return 2**31 - 1
27        return num