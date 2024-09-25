# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # storage implementation
        # visited=set()
        # cur=head
        # while cur:
        #     if cur in visited:
        #         return True
        #     visited.add(cur)
        #     cur=cur.next
        # return False

        # fast and slow implementation
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                return True
        return False
        