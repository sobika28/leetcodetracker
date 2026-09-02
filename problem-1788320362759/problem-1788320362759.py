# Last updated: 9/2/2026, 9:09:22 AM
1class Solution:
2    def swapPairs(self, head):
3        dummy = ListNode(0)
4        dummy.next = head
5
6        prev = dummy
7
8        while prev.next and prev.next.next:
9            first = prev.next
10            second = first.next
11
12            first.next = second.next
13            second.next = first
14            prev.next = second
15            prev = first
16        return dummy.next