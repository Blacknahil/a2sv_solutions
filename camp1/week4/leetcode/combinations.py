from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        collection=[i for i in range(1,n+1)]
        ans=[]
        def dfs(idx,cur):
            if len(cur)==k:
                ans.append(cur[:])
                return
            if idx>=n:
                return 
            dfs(idx+1,cur+[collection[idx]])
            dfs(idx+1,cur)
        dfs(0,[])
        return ans