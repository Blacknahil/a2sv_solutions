class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left=0
        right=len(nums)-1
        if not nums:
            return [-1,-1]
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid
        if nums[left]!=target:
            return [-1,-1]
        start,end=left,left
        while start>0 and nums[start-1]==target:
            start-=1
        while end+1<=len(nums)-1 and nums[end+1]==target:
            end+=1
        return [start,end]
