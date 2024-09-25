# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        forward=head
        dummy=ListNode(0,head)
        for _ in range(n-1):
            forward=forward.next
        prev=dummy
        back=dummy.next
        while forward.next:
            forward=forward.next
            prev=back
            back=back.next
        if back:
            prev.next=back.next
        return dummy.next
        