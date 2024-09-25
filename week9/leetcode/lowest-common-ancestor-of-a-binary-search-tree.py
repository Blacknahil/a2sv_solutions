# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findleast(node):
            if node.val>p.val and node.val>q.val:
                return findleast(node.left)
                #go left
            if node.val<p.val and node.val<q.val:
                return findleast(node.right)
                #go right
            else:
                return node
        return findleast(root)
        