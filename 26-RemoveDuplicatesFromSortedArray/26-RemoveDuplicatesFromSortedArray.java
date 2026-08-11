// Last updated: 8/11/2026, 12:25:16 PM
class Solution {
    public int removeDuplicates(int[] nums) {
        int k=0;
      for(int x:nums)  {
        if(k==0 || x!=nums[k-1]){
            nums[k++]=x;
        }
      }
      return k;
    }
}