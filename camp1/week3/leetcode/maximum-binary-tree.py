# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def construct(left,right):
            if left>right:
                return None
            if left==right:
                return TreeNode(nums[left])
            m=left
            for i in range(left,right+1):
                if nums[i]>nums[m]:
                    m=i
            node=TreeNode(nums[m])
            node.left=construct(left,m-1)
            node.right=construct(m+1,right)
            return node
        return construct(0,len(nums)-1)
        