# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head):
        zerohead = ListNode(-1)
        onehead = ListNode(-1)
        twohead = ListNode(-1)
        zero =  zerohead
        one = onehead
        two = twohead
        temp = head
        while temp :
            if temp.val == 0:
                zero.next = temp
                zero = temp
            elif temp.val == 1:
                one.next = temp 
                one = temp
            else:
                two.next = temp
                two = temp
            temp = temp.next
        zero.next = onehead.next if onehead.next else twohead.next
        one.next = twohead.next
        two.next = None
        newhead = zerohead.next
        return newhead 
