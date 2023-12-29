class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        for i in range(len(nums)):
            for j in range(len(nums)-1-i):
                if int(nums[j] + nums[j+1]) < int(nums[j+1] + nums[j]):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        nums=str(int("".join(nums)))
        return nums
        