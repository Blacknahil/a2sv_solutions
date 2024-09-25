# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        _sum=0
        def dfs(node,before):
            nonlocal _sum
            if not node:
                return 
            before=before*10 + node.val
            if not node.left and not node.right:
                _sum+=before
            dfs(node.left,before)
            dfs(node.right,before)
        dfs(root,0)
        return _sum
            

        