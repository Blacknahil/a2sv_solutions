# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        node1=root1
        node2=root2
        if node2 is None:
            return node1
        if node1 is None:
            return node2
        node1.val=node1.val+node2.val
        node1.left=self.mergeTrees(node1.left,node2.left)
        node1.right=self.mergeTrees(node1.right,node2.right)
        return node1
        
