# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        q=deque([(root,1)])
        _max=0
        while q:
            left=q[0][1]
            right=q[-1][1]
            _max=max(_max,right-left+1)
            for i in range(len(q)):
                node,pos=q.popleft()
                if node.left:
                    q.append((node.left,pos*2))
                if node.right:
                    q.append((node.right,pos*2 +1 ))
        return _max      