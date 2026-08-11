// Last updated: 8/11/2026, 12:25:24 PM
class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix=strs[0];
       // String end =strs[strs.length-1];
        for(String s:strs){
            while(s.indexOf(prefix)!=0){
                prefix = prefix.substring(0,prefix.length()-1);
            }
           
        }
        return prefix;
    }
}