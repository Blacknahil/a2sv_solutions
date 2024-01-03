class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        slow,fast=0,len(nums)-1
        nums.sort()
        count=0
        while fast>slow :
            if nums[slow] + nums[fast]< target:
                count+=fast-slow
                slow+=1
            else:
                fast-=1
        return count
        

        