// Last updated: 8/11/2026, 12:25:39 PM
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int longest = 0;
        
        
        for(int i=0;i<s.length();i++){
            HashSet<Character> set = new HashSet<>();
            for(int j =i;j<s.length();j++){
                if(set.contains(s.charAt(j))){
                 break;
                 }
                 else{
                 set.add(s.charAt(j));
                 }
                 longest = Math.max(longest, j-i+1);
            }
        }
       
         return longest;
        
    }
}