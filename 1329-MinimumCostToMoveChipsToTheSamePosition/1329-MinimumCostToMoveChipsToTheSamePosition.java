// Last updated: 8/11/2026, 12:21:47 PM
class Solution {
    public int minCostToMoveChips(int[] position) {
        int evencount= 0;
        int oddcount = 0;
        for(int i=0;i<position.length;i++){
            if(position[i]% 2==0){
                 evencount++;
            }
            else{
                oddcount++;
            }
        }
        return Integer.min(evencount,oddcount);
    }     
}
