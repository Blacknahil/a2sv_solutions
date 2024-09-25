# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(node1,node2):
            #till node 1 reaches the end reverse
            cur=node1
            prev=None
            while cur!=node2:
                nex=cur.next
                cur.next=prev
                prev=cur
                cur=nex
                nex=nex.next
            cur.next=prev
            Tail=cur
            Head=node1
            return Head,Tail

        
        prev=None
        cur=head
        index=1
        sub_tail=None
        sub_head=None
        while cur:
            if sub_tail and sub_head:
                break
            if left==index:
                sub_tail=cur
                tail_prev=prev
            if right==index:
                sub_head=cur
                head_next=cur.next
            prev=cur
            cur=cur.next
            index+=1
        newHead,newTail=reverse(sub_tail,sub_head)

        if tail_prev:
            tail_prev.next=newTail
        else:
            head=newTail
        if head_next:
            newHead.next=head_next
        return head
            
        