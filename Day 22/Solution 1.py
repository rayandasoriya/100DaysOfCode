# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        if head and head.next:
            n = head.next
            head.next = self.swapPairs(n.next)
            n.next = head
            return n
        return head
