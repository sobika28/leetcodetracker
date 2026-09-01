# Last updated: 9/1/2026, 9:24:26 PM
1class Solution(object):
2    def searchInsert(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: int
7        """
8        start = 0
9        end = len(nums) -1
10        mid = 0
11
12        while(start <= end): 
13            mid = start + ( end - start)/2
14            if(nums[mid] == target): 
15                return mid
16            elif(nums[mid] < target): 
17                start = mid + 1
18            else:
19                end = mid - 1
20    
21        return start
22        