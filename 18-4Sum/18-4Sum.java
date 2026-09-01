// Last updated: 9/1/2026, 10:14:25 PM
1class Solution {
2    public List<List<Integer>> fourSum(int[] nums, int target) {
3        List<List<Integer>> ans = new ArrayList<>();
4
5        int n = nums.length;
6        Arrays.sort(nums);
7
8        for (int i = 0; i < n - 3; i++) {
9            if (i > 0 && nums[i] == nums[i - 1])
10                continue;
11            for (int j = i + 1; j < n - 2; j++) {
12                if (j > i + 1 && nums[j] == nums[j - 1])
13                    continue;
14                int start = j + 1;
15                int end = n - 1;
16                while (start < end) {
17                    long sum = (long) nums[i]+nums[j]+nums[start]+nums[end];
18
19                    if (sum == target) {
20                        ans.add(Arrays.asList(nums[i],nums[j],nums[start],nums[end]));
21
22                        start++;
23                        end--;
24                    
25                        while (start < end && nums[start] == nums[start - 1]) 
26                            start++;
27                        
28                        while (start < end && nums[end] == nums[end + 1]) 
29                            end--;
30                    } else if (sum < target) {
31                        start++;
32                    } else {
33                        end--;
34                    }
35                }
36            }
37        }
38        return ans;
39    }
40}