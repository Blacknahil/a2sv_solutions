class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # lets use bubble sort
        n=len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j]> nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums
