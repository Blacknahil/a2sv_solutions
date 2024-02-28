# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic=defaultdict(int)
        def traverse(node):
            if not node:
                return
            dic[node.val]+=1
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        ans=[]
        maxf=max(dic.values())
        for key in dic:
            if dic[key]==maxf:
                ans.append(key)
        return ans
        