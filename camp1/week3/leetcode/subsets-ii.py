class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        nums.sort()
        def backtrack(start,cur):
            ans.add(tuple(cur[:]))
            for i in range(start,len(nums)):
                cur.append(nums[i])
                backtrack(i+1,cur)
                cur.pop()
        backtrack(0,[])
        return ans
        