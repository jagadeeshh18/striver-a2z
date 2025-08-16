# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        while temp :
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev     
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow , fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        newnode = self.reverseList(slow.next)
        first,second = head,newnode
        while second != None:
            if first.val != second.val :
                 self.reverseList(newnode)
                 return False
            first = first.next
            second = second.next
        self.reverseList(newnode)
        return True



        
