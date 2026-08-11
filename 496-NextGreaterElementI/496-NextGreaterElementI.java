// Last updated: 8/11/2026, 12:22:34 PM
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] a=new int[nums1.length];
        for(int i=0;i<nums1.length;i++){
            int greIdx = -1,j =nums2.length -1;
            while(j >=0 && nums2[j]!=nums1[i])
            {
                if(nums2[j]>nums1[i]){
                    greIdx=nums2[j];
                }
                j--;
            }
            a[i]=greIdx;
        }
        return a;
    }
}