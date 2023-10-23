class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index=0
        next_num=0
        while index<len(nums):
            if nums[index]!=0:
                nums[index],nums[next_num]=nums[next_num],nums[index]
                next_num+=1
            index+=1
