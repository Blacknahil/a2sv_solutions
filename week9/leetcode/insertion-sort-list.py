# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls=[]
        cur=head
        while cur:
            ls.append(cur)
            cur=cur.next
        ls.sort(key=lambda node:node.val)
        head=ls[0]
        for i in range(len(ls)-1):
            cur=ls[i]
            nex=ls[i+1]
            cur.next=nex
        ls[-1].next=None
        return head
        