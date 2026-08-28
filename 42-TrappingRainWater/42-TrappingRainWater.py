# Last updated: 8/28/2026, 10:14:05 AM
1class Solution(object):
2    def trap(self, height):
3        
4        left = 0
5        right = len(height) - 1
6        leftmax = 0
7        rightmax = 0
8        water = 0
9
10        while left < right:
11            if height[left] <= height[right]:
12                if height[left] >= leftmax:
13                    leftmax = height[left]
14                else:
15                    water += leftmax - height[left]
16                left += 1
17            else:
18                if height[right] >= rightmax:
19                    rightmax = height[right]
20                else:
21                    water += rightmax - height[right]
22                right -= 1
23
24        return water
25        