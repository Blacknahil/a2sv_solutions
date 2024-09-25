# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_less=ListNode(0)
        dummy_more=ListNode(1)
        less=dummy_less
        more=dummy_more
        cur=head
        while cur:
            if cur.val>=x:
                more.next=cur
                more=more.next
            else:
                less.next=cur
                less=less.next
            cur=cur.next
        more.next=None
        less.next=dummy_more.next
        return dummy_less.next
        