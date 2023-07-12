# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        while current is not None:
            pointer=current
            _min=current
            while pointer:
                if pointer.val<_min.val:
                    _min=pointer
                pointer=pointer.next
            current.val,_min.val=_min.val,current.val
            current=current.next
        return head
            

            

