# Last updated: 9/2/2026, 9:20:15 AM
1from collections import deque
2
3class Solution:
4    def maxSlidingWindow(self, nums, k):
5        dq = deque()
6        ans = []
7
8        for i in range(len(nums)):
9
10            if dq and dq[0] <= i - k:
11                dq.popleft()
12
13            while dq and nums[dq[-1]] <= nums[i]:
14                dq.pop()
15
16            dq.append(i)
17            if i >= k - 1:
18                ans.append(nums[dq[0]])
19
20        return ans