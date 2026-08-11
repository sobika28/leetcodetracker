// Last updated: 8/11/2026, 12:23:41 PM
class Solution {
    public int findKthLargest(int[] nums, int k) {
        Arrays.sort(nums);
        int start =0,end = nums.length-1;
        while(start<end){
            int temp = nums[start];
            nums[start]=nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
        return nums[k-1];
    }
}