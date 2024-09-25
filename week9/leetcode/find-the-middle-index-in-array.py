class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum=0
        right_sum=sum(nums)
        for i in range(len(nums)):
            right_sum-=nums[i]
            if right_sum==left_sum:
                return i
            left_sum+=nums[i]
        return -1
        