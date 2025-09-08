# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1=l1
        t2 = l2
        carry = 0
        dum = ListNode(-1)
        curr = dum
        while t1 or t2:
            summ = carry
            if t1:
                summ+=t1.val
            if t2:
                summ += t2.val
            new = ListNode(summ % 10)
            carry = summ // 10
            curr.next = new
            curr = curr.next
            if t1:
                t1 = t1.next
            if t2:
                t2 = t2.next
        if carry:
            neww = ListNode(carry)
            curr.next = neww
        return dum.next
