// Last updated: 8/11/2026, 12:24:25 PM
class Solution {
    public int longestConsecutive(int[] nums) {
       if(nums.length==0){
        return 0;
       }
       Arrays.sort(nums);
       int len =1;
       int currentlen =1;
        for(int i=1;i<nums.length;i++){
                if(nums[i] == nums[i-1]){
                   continue;
                }
                else if(nums[i]==nums[i-1]+1){
                    currentlen++;
                }
                else{
                    len = Math.max(len,currentlen);
                    currentlen =1;
                }
            
        }
        return Math.max(len,currentlen);
    }
}