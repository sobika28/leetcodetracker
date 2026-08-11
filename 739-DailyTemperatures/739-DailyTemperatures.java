// Last updated: 8/11/2026, 12:22:21 PM
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n=temperatures.length;
        int []ans=new int[n];
        Stack<Integer> stack=new Stack<>();
        for(int i=0;i<n;i++){
            while(!stack.isEmpty() && temperatures[i]>temperatures[stack.peek()]){
                int idx=stack.pop();
                ans[idx]=i-idx;
            }
            stack.push(i);
        }
        return ans;
    }
}