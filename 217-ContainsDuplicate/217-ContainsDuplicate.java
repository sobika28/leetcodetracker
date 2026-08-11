// Last updated: 8/11/2026, 12:23:38 PM
class Solution {
    public boolean containsDuplicate(int[] nums) {
       HashSet<Integer> set =new HashSet<Integer>();
       for(int num:nums){
        if(set.contains(num)){
            return true;
        }
        set.add(num);

       }
       return false;

    }
}