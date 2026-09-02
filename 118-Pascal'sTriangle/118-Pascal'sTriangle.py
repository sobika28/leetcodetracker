# Last updated: 9/2/2026, 9:24:10 AM
1class Solution:
2    def generate(self, numRows):
3        ans = []
4
5        for i in range(numRows):
6            row = [1] * (i + 1)
7
8            for j in range(1, i):
9                row[j] = ans[i - 1][j - 1] + ans[i - 1][j]
10
11            ans.append(row)
12
13        return ans