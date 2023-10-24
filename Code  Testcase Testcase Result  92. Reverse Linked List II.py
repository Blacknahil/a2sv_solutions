# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy=ListNode(0,head)
        left_prev,cur=dummy,head
        for _ in range(left-1):
            left_prev=cur
            cur=cur.next
        prev=None
        for _ in range(right-left+1):
            temp=cur.next
            cur.next=prev
            prev,cur=cur,temp
        left_prev.next.next=cur
        left_prev.next=prev
        return dummy.next

        
