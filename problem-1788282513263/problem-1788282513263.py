# Last updated: 9/1/2026, 10:38:33 PM
1class Solution:
2    def maxProfit(self, prices):
3        buy1 = float('-inf')
4        sell1 = 0
5        buy2 = float('-inf')
6        sell2 = 0
7        for price in prices:
8            buy1 = max(buy1, -price)
9            sell1 = max(sell1, buy1 + price)
10            buy2 = max(buy2, sell1 - price)
11            sell2 = max(sell2, buy2 + price)
12        return sell2