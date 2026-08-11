// Last updated: 8/11/2026, 12:20:55 PM
class Solution {
    public int averageValue(int[] nums) {
        int even = 0;
        int count=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]%6==0){
                    even+=nums[i];
                    count++;
                    
                
            }
        }
        if(count==0){
        return 0;
        }
        return even/count;

    }
}