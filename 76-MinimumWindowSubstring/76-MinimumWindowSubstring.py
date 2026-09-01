# Last updated: 9/1/2026, 10:04:59 PM
1class Solution:
2    def minWindow(self, s, t):
3        need, missing = collections.Counter(t), len(t)
4        i = I = J = 0
5        for j, c in enumerate(s, 1):
6            missing -= need[c] > 0
7            need[c] -= 1
8            if not missing:
9              while i < j and need[s[i]] < 0:
10                need[s[i]] += 1
11                i += 1
12              if not J or j - i <= J - I:
13                I, J = i, j
14        return s[I:J]