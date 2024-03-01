# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        ls=[]

        def inorder(node):

            if not node:
                return
            inorder(node.left)
            ls.append(node.val)
            inorder(node.right)

        inorder(root)
        
        def balance(left,right):
            if left>right:
                return None

            if left==right:
                return TreeNode(ls[left])

            middle=(left+right)//2
            new=TreeNode(ls[middle])
            new.left=balance(left,middle-1)
            new.right=balance(middle+1,right)

            return new

        return balance(0,len(ls)-1)