# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validating(node,mini,maxi):
            if not node:
                return True

            elif node.val <=mini or maxi<=node.val:
                return False
            return validating(node.left,mini,node.val) and validating(node.right,node.val,maxi)
        return validating(root,float('-inf'),float('inf'))
        
