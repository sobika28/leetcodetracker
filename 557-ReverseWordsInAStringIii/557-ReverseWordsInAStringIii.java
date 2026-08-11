// Last updated: 8/11/2026, 12:22:32 PM
class Solution {
    public String reverseWords(String s) {
        String[] words=s.split(" ");
        StringBuilder result=new StringBuilder();
        for(String word:words){
            StringBuilder reversedWord =new StringBuilder(word);
            reversedWord.reverse();
            result.append(reversedWord).append(" ");
        }
        return result.toString().trim();
    }
}