# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def checkEach(node1,node2):
            if not node1 and not node2:
                return True
            if node1 and node2 and node1.val==node2.val:
                return checkEach(node1.left,node2.left) and checkEach(node1.right,node2.right)
            else:
                return False
        return checkEach(p,q)