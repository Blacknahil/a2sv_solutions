class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        nums.sort()
        close=nums[1]+nums[2] +nums[0]
            
        for left in range(len(nums)-2):
            pt=left+1
            right=len(nums)-1
            while pt<right:
                cur=nums[left] + nums[pt] + nums[right]
                if abs(cur-target)<abs(close-target):
                    close=cur
                elif cur>target:
                    right-=1
                elif cur<target:
                    pt+=1
                else:
                    return target
        return close
        