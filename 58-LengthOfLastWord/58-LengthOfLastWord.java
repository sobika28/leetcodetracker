// Last updated: 8/11/2026, 12:25:00 PM
class Solution {
    public int lengthOfLastWord(String s) {
        int end=s.length()-1;
        while(end>=0 && s.charAt(end)==' '){
            end--;
            }
            int start=end;
            while(start>=0 && s.charAt(start)!=' '){
                start--;
            }
            return end-start;
            
    }
}