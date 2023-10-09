# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        st=''
        def preorder(node):
            nonlocal st
            if node is None:
                return
            st+=str(node.val)
            if node.left or node.right:
                st+="("
                preorder(node.left)
                st+=")"
            if node.right or node.right:
                st+='('
                preorder(node.right)
                st+=')'
        preorder(root)
        return st
