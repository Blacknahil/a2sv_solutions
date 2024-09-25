# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy=ListNode(0)
        head2=dummy
        cur=head
        while cur:
            head2.next=ListNode(cur.val)
            cur=cur.next
            head2=head2.next
        prev=None
        cur=dummy.next
        while cur.next:
            nex=cur.next
            cur.next=prev
            prev=cur
            cur=nex
            nex=nex.next
        cur.next=prev
        head2=cur
        while head and head2:
            if head.val !=head2.val:
                return False
            head=head.next
            head2=head2.next
        return True

        