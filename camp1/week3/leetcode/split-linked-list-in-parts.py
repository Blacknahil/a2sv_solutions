# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n=0
        cur=head
        while cur:
            n+=1
            cur=cur.next
        offset=n%k
        size=n//k
        ans=[]
        def traverse(node,k):
            nonlocal offset
            nonlocal size
            if not k:
                return
            count=size 
            if offset:
                count+=1
                offset-=1
            ans.append(node)
            temp=node
            while node and count:
                temp=node
                node=node.next
                count-=1
            if temp:
                temp.next=None
            traverse(node,k-1)
        traverse(head,k)

        return ans