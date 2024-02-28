# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def divide(left,right):
            if left>=len(nums) or left>right or right<0:
                return None
            if left==right:
                return TreeNode(nums[left])
            middle=(left+right)//2
            new=TreeNode(nums[middle])
            new.left=divide(left,middle-1)
            new.right=divide(middle+1,right)
            return new
        return divide(0,len(nums)-1)
        