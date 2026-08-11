// Last updated: 8/11/2026, 12:20:56 PM
class Solution {
    public int[] applyOperations(int[] nums) {
        int[] temp =new int[nums.length];
        int k=0;
        for(int i=0;i<nums.length;i++){
             if(i==nums.length-1){
               temp[k]=nums[i] ;
               break;
            }
            if(nums[i]!=0){
         if(nums[i]==nums[i+1]){
        temp[k]=nums[i]*2;
        i=i+1;
         }
         
         else {
         temp[k]=nums[i];
         }
         
         k++;} 
        } return temp;
    }
}