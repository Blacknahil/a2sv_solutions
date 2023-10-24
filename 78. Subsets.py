class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power=[]
        sub=[]
        def backtrack(i):
            if i>=len(nums):
                power.append(sub.copy())
                return
            sub.append(nums[i])
            backtrack(i+1)

            sub.pop()
            backtrack(i+1)
        backtrack(0)
        return power
