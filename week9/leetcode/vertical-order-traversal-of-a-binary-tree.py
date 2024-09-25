# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic=defaultdict(list)
        def dfs(node,col,row):
            if not node:
                return 
            dic[col].append((node.val,row))
            dfs(node.left,col-1,row+1)
            dfs(node.right,col+1,row+1)
        dfs(root,0,0)
        offset=min(dic.keys())
        _max=max(dic.keys())
        ans=[0 for _ in range(-offset+_max+1)]
        for key in dic:
            inside=dic[key]
            inside.sort(key=lambda x:(x[1],x[0]))
            res=[]
            for one in inside:
                res.append(one[0])
            ans[key-offset]=res
        return  ans