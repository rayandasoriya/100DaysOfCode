# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return
        
        loop=head
        c=1
        while loop.next!=None:
            loop=loop.next
            c=c+1
        loop.next=head
        k=k%c
        k=c-k
        while k>0:
            head=head.next
            loop=loop.next
            k-=1
        loop.next=None
        return head
