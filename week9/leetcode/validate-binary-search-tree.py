# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node,_max,_min):
            if not node:
                return True
            if node.val>=_max:
                return False
            if node.val<=_min:
                return False
            return validate(node.left,node.val,_min) and validate(node.right,_max,node.val)
        return validate(root,float("inf"),float("-inf"))
        