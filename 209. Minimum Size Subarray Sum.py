class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_width=len(nums)+1
        left=0
        _sum=0
        for right in range(len(nums)):
            _sum+=nums[right]
            while _sum>=target:
                _sum-=nums[left]
                min_width=min(min_width,right-left+1)
                left+=1
        if min_width==len(nums)+1:
             return 0
        else:
            return min_width
