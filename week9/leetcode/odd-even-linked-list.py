# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_odd=ListNode(1)
        dummy_even=ListNode(0)
        even=dummy_even
        odd=dummy_odd
        cur=head
        index=0
        while cur:
            if index%2==0:
                even.next=cur
                even=cur
            else:
                odd.next=cur
                odd=cur
            index+=1
            cur=cur.next
        odd.next=None
        even.next=dummy_odd.next
        return dummy_even.next

        