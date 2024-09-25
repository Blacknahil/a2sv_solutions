# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # [[3],[20,9],[10,15,7],[7,6,5,3,1]]
        if not root:
            return []
        q=deque([root])
        ans=[]
        dxn="left"
        while q:
            res=[]
            for _ in range(len(q)):
                node=q.popleft()
                if not node:
                    continue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                res.append(node.val)
            if dxn=="left":
                ans.append(res)
                dxn="right"
            else:
                ans.append(res[::-1])
                dxn="left"

        return ans