 #Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr=dummy=ListNode()
        carry=0
        s1=s2=""
        while l1:
            s1+=str(l1.val)
            l1=l1.next
        while l2:
            s2+=str(l2.val)
            l2=l2.next
        n3=int(s1[::-1])+int(s2[::-1])
        n4=str(n3)
        n5=n4[::-1]
        for i in n5:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next
