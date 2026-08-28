# Last updated: 8/28/2026, 10:18:02 AM
1class Solution:
2    def longestPalindrome(self, s):
3        ans = ""
4
5        for i in range(len(s)):
6           
7            l = r = i
8            while l >= 0 and r < len(s) and s[l] == s[r]:
9                if r - l + 1 > len(ans):
10                    ans = s[l:r+1]
11                l -= 1
12                r += 1
13
14            l = i
15            r = i + 1
16            while l >= 0 and r < len(s) and s[l] == s[r]:
17                if r - l + 1 > len(ans):
18                    ans = s[l:r+1]
19                l -= 1
20                r += 1
21
22        return ans