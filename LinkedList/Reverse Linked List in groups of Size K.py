# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def kthnode(self,temp,k):
        k-=1
        while temp and k >0:
            k-=1
            temp = temp.next
        return temp
    def reverse(self,temp):
        prev = None
        while temp:
            front = temp.next
            temp.next=prev
            prev = temp
            temp = front
        return prev
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prev = None
        while temp:
            kth = self.kthnode(temp,k)
            if kth is None:
                if prev:
                    prev.next = temp
                    break
            nextnode = kth.next
            kth.next = None
            rev = self.reverse(temp)
            if temp == head:
                head = rev
            else:
                prev.next = rev
            prev = temp
            temp = nextnode
        return head


