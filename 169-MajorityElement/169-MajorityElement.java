// Last updated: 8/11/2026, 12:24:02 PM
class Solution {
    public int majorityElement(int[] nums) {
        int candidate = 0, count = 0;

        for (int num : nums) {
            if (count == 0) {
                candidate = num; 
            }
            count += (num == candidate) ? 1 : -1;
        }
        return candidate;
    }
}
