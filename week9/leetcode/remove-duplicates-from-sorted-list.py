# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        if not cur:
            return
        nxt=cur.next
        while cur and nxt:
            if cur.val==nxt.val:
                nxt=nxt.next
            else:
                cur.next=nxt
                cur=nxt
                nxt=nxt.next
        cur.next=None
        return head

        
        