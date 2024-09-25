# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def findIntersection(headA,headB):
            while headA and headB:
                if headA==headB:
                    return headA
                headA=headA.next
                headB=headB.next
            return None
        lenA=0
        lenB=0
        curA=headA
        curB=headB
        #getting the length of the lists
        while curA:
            lenA+=1
            curA=curA.next
        while curB:
            lenB+=1
            curB=curB.next
        
        if lenA>lenB:
            temp_node=headA
        else:
            temp_node=headB
        dist=abs(lenA-lenB)
        for i in range(dist):
            temp_node=temp_node.next
        if lenA<lenB:
            return findIntersection(headA,temp_node)
        elif lenA>lenB:
            return findIntersection(temp_node,headB)
        else:
            return findIntersection(headA,headB)

        