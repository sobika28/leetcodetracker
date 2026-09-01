// Last updated: 9/1/2026, 10:12:08 PM
1class Solution {
2    public static int largestRectangleArea(int[] height) {
3    if (height == null || height.length == 0) {
4        return 0;
5    }
6    int[] lessFromLeft = new int[height.length]; // idx of the first bar the left that is lower than current
7    int[] lessFromRight = new int[height.length]; // idx of the first bar the right that is lower than current
8    lessFromRight[height.length - 1] = height.length;
9    lessFromLeft[0] = -1;
10
11    for (int i = 1; i < height.length; i++) {
12        int p = i - 1;
13
14        while (p >= 0 && height[p] >= height[i]) {
15            p = lessFromLeft[p];
16        }
17        lessFromLeft[i] = p;
18    }
19
20    for (int i = height.length - 2; i >= 0; i--) {
21        int p = i + 1;
22
23        while (p < height.length && height[p] >= height[i]) {
24            p = lessFromRight[p];
25        }
26        lessFromRight[i] = p;
27    }
28
29    int maxArea = 0;
30    for (int i = 0; i < height.length; i++) {
31        maxArea = Math.max(maxArea, height[i] * (lessFromRight[i] - lessFromLeft[i] - 1));
32    }
33
34    return maxArea;
35}
36}