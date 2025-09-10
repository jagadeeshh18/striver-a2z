# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def newnode(self,head,k):
        cnt = 1
        temp = head
        while temp:
            if cnt == k :
                return temp
            cnt+=1
            temp = temp.next
        return temp
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head
        lenn = 1
        tail = head
        while tail.next:
            lenn+=1
            tail = tail.next
        
        if k % lenn == 0:
            return head
        
        k = k % lenn
        tail.next = head
        last = self.newnode(head,lenn - k)
        head = last.next
        last.next = None
        return head
        
