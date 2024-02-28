# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(node,curmax,curmin):
            if not node:
                return curmax-curmin
            curmax=max(curmax,node.val)
            curmin=min(curmin,node.val)

            left=dfs(node.left,curmax,curmin)
            right=dfs(node.right,curmax,curmin)
            
            return max(left,right)

        return dfs(root,root.val,root.val)