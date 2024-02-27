class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=set()

        def dfs(start,cur):
            ans.add(tuple(cur))
            for i in range(start,len(nums)):
                cur.append(nums[i])
                dfs(i+1,cur)
                cur.pop()
        dfs(0,[])
        return ans
        