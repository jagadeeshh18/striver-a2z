# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findmiddle(self,head):
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self,lefthead,righthead):
        t1 = lefthead
        t2 = righthead
        dummy = ListNode(-1)
        temp = dummy
        while t1 and t2:
            if t1.val < t2.val:
                temp.next = t1
                temp = t1
                t1 = t1.next
            else:
                temp.next = t2
                temp = t2
                t2=t2.next
        if t1:
            temp.next = t1
        else:
            temp.next = t2
        return dummy.next
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        mid = self.findmiddle(head)
        lefthead = head
        righthead = mid.next
        mid.next = None
        lefthead = self.sortList(lefthead)
        righthead = self.sortList(righthead)
        return self.merge(lefthead,righthead)
        
