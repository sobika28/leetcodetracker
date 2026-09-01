# Last updated: 9/1/2026, 9:18:52 PM
1class Solution:
2    def isMatch(self, s, p):
3        m = len(s)
4        n = len(p)
5
6        dp = [[False] * (n + 1) for _ in range(m + 1)]
7
8        dp[0][0] = True
9
10        # Patterns like a*, a*b*, a*b*c* can match empty string
11        for j in range(2, n + 1):
12            if p[j - 1] == '*':
13                dp[0][j] = dp[0][j - 2]
14
15        for i in range(1, m + 1):
16            for j in range(1, n + 1):
17
18                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
19                    dp[i][j] = dp[i - 1][j - 1]
20
21                elif p[j - 1] == '*':
22                    # Use * zero times
23                    dp[i][j] = dp[i][j - 2]
24
25                    # Use * one or more times
26                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
27                        dp[i][j] = dp[i][j] or dp[i - 1][j]
28
29        return dp[m][n]