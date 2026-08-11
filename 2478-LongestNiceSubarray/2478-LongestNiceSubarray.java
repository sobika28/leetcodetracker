// Last updated: 8/11/2026, 12:21:00 PM
class Solution {
    public int longestNiceSubarray(int[] nums) {
          int ans = 0;
    int used = 0;

    for (int l = 0, r = 0; r < nums.length; ++r) {
      while ((used & nums[r]) > 0)
        used ^= nums[l++];
      used |= nums[r];
      ans = Math.max(ans, r - l + 1);
    }

    return ans;
    }
}