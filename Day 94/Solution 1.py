# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        dummy = pre = ListNode(0)
        dummy.next = head
        for _ in xrange(m-1):
            pre = pre.next
        cur= pre.next
        node = None
        for _ in xrange(n-m+1):
            nxt = cur.next
            cur.next = node
            node = cur
            cur= nxt
        pre.next.next = cur
        pre.next = node
        return dummy.next
