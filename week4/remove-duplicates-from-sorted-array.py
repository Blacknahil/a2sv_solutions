class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=0
        right=1
        if len(nums)<=1:
            return len(nums)
        while right < len(nums):
            if nums[left] != nums[right]:
                left+=1
                nums[left]=nums[right]
            right+=1
        return left + 1
        