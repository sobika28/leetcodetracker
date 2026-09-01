# Last updated: 9/1/2026, 10:07:18 PM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution(object):
8    def addTwoNumbers(self, l1, l2):
9        """
10        :type l1: ListNode
11        :type l2: ListNode
12        :rtype: ListNode
13        """
14       
15        dummy = ListNode(0)
16        curr = dummy
17        carry = 0
18
19       
20        while l1 or l2 or carry:
21            
22            val1 = l1.val if l1 else 0
23            val2 = l2.val if l2 else 0
24            
25            total = val1 + val2 + carry
26            carry = total // 10
27        
28            curr.next = ListNode(total % 10)
29            
30            curr = curr.next
31            if l1: l1 = l1.next
32            if l2: l2 = l2.next
33            
34        return dummy.next