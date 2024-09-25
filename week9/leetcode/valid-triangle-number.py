class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count=0
        nums.sort()
        for i in range(len(nums)-1,1,-1):
            goal=nums[i]
            left=0
            right=i-1
            while left<right:
                if nums[left] + nums[right]>goal:
                    count+=(right-left)
                    right-=1
                else:
                    left+=1
        return count