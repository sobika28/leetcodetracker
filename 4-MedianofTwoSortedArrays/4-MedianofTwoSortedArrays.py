# Last updated: 9/1/2026, 9:11:34 PM
1class Solution:
2    def findMedianSortedArrays(self, nums1, nums2):
3        merged = nums1 + nums2
4        merged.sort()
5        total = len(merged)
6        if total % 2 == 1:
7            return float(merged[total // 2])
8        else:
9            middle1 = merged[total // 2 - 1]
10            middle2 = merged[total // 2]
11            return (float(middle1) + float(middle2)) / 2.0