class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_window=0
        left=0
        zeros=1
        for right in range(len(nums)):
            if nums[right]==0:
                zeros-=1
            while left <= right and zeros<0:
                if nums[left]==0:
                    zeros+=1
                left+=1
            max_window=max(max_window,right-left)
        return max_window
   # 0,1,1,1,0,1,1,0,1]
   # ^
   #         ^