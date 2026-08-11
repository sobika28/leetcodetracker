// Last updated: 8/11/2026, 12:22:57 PM
class Solution {
    public void reverseString(char[] s) {
             int left = 0; 
        int right = s.length - 1; 
        while (left < right) {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
    }
}
}