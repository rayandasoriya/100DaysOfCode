# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        numbers = {1: '', 2: ''}
        while l1 is not None or l2 is not None:
            if l1 is not None:
                numbers[1] = str(l1.val) + numbers[1]
                l1 = l1.next
            if l2 is not None:
                numbers[2] = str(l2.val) + numbers[2]
                l2 = l2.next
    
        head = l3 = ListNode(None)
        for x in [int(x) for x in str(int(numbers[1]) + int(numbers[2]))][::-1]:
            if l3.val is None:
                l3.val = x
            else:
                l3.next = ListNode(x)
                l3 = l3.next

return head
