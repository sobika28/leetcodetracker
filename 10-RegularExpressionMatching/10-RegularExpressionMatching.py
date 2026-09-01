# Last updated: 9/1/2026, 9:19:39 PM
1class Solution:
2    def isMatch(self, s, p):
3        m = len(s)
4        n = len(p)
5        dp = [[False] * (n + 1) for _ in range(m + 1)]
6        dp[0][0] = True
7        for j in range(2, n + 1):
8            if p[j - 1] == '*':
9                dp[0][j] = dp[0][j - 2]
10        for i in range(1, m + 1):
11            for j in range(1, n + 1):
12                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
13                    dp[i][j] = dp[i - 1][j - 1]
14                elif p[j - 1] == '*':
15                    dp[i][j] = dp[i][j - 2]
16                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
17                        dp[i][j] = dp[i][j] or dp[i - 1][j]
18        return dp[m][n]