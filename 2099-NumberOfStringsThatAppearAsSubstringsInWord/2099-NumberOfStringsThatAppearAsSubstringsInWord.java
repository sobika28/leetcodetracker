// Last updated: 8/11/2026, 12:21:17 PM
class Solution {
    public int numOfStrings(String[] patterns, String word) {
        int count =0;
        for(String s: patterns)
             if(word.indexOf(s)!=-1)
               count++;
        return count;
    }
}