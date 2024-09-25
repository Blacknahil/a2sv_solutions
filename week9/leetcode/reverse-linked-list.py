# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        cur=head
        prev=None
        while cur and cur.next:
            nex=cur.next#going to be cur
            cur.next=prev
            prev=cur
            cur=nex
        if cur:
            cur.next=prev
            dummy.next=cur
        return dummy.next
        
        