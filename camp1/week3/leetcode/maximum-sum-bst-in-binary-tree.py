# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans=float("-inf")
        def dfs(node):
            nonlocal ans
            if not node:
                return 
            if not node.left:
                left_is_BST,left_min,left_max,left_sum=True,node.val,node.val-1,0
            else:
                left_is_BST,left_min,left_max,left_sum=dfs(node.left)
            if not node.right:
                right_is_BST,right_min,right_max,right_sum=True,node.val+1,node.val,0
            else:
                right_is_BST,right_min,right_max,right_sum=dfs(node.right)
            
            cur_sum=node.val + left_sum+right_sum
            cur_max=max(right_max,node.val)
            cur_min=min(left_min,node.val)
            if left_is_BST and right_is_BST and right_min>node.val>left_max:
                cur_is_BST=True
            else:
                cur_is_BST=False
            if cur_is_BST:
                ans=max(ans,cur_sum)
            return (cur_is_BST,cur_min,cur_max,cur_sum)
        dfs(root)
        return max(0,ans)
            