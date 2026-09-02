// Last updated: 9/2/2026, 9:35:04 AM
1class Solution {
2    public boolean searchMatrix(int[][] matrix, int target) {
3
4        for (int i = 0; i < matrix.length; i++) {
5
6            for (int j = 0; j < matrix[0].length; j++) {
7
8                if (matrix[i][j] == target) {
9                    return true;
10                }
11            }
12        }
13
14        return false;
15    }
16}