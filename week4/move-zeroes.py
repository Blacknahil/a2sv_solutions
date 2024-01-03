class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        valid=0
        for pointer in range(len(nums)):
            if nums[pointer]:
                nums[valid],nums[pointer]=nums[pointer],nums[valid]
                valid+=1
        
        