// Last updated: 8/11/2026, 12:22:49 PM
class Solution {
    public int lastRemaining(int n) {
        if(n==1)
        return 1;
         return 2*(1+n/2-lastRemaining(n/2));
    }
     
}