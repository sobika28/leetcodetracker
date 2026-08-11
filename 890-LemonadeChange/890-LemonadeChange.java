// Last updated: 8/11/2026, 12:22:08 PM
class Solution {
    public boolean lemonadeChange(int[] bills) {
    
        int c_5 = 0, c_10 = 0;

        for (int i = 0; i < bills.length; i++) {
            if (bills[i] == 5) {
                c_5++;
            } 
            else if (bills[i] == 10) {
                if (c_5 >= 1) {
                    c_5--;
                    c_10++;
                } 
                else {
                    return false;
                }
            } 
            else if (bills[i] == 20) {
                if (c_10 >= 1 && c_5 >= 1) {
                    c_10--;
                    c_5--;
                } 
                else if (c_5 >= 3) {
                    c_5 -= 3;
                } 
                else {
                    return false;
                }
            }
        }

        return true;
    }
    }

