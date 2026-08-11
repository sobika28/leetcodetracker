// Last updated: 8/11/2026, 12:24:21 PM
class Solution {
    public int singleNumber(int[] nums) {
        int res=0;
        for(int num:nums){
            
            res^=num;
        }
        return res;
    }
}