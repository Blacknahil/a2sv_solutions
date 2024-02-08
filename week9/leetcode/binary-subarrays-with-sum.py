class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(nums,goal):
            left=0
            count=0
            cur=0
            for right in range(len(nums)):
                cur+=nums[right]
                while cur>goal and left<=right:
                    cur-=nums[left]
                    left+=1
                count+=right-left+1
            return count
        return atmost(nums,goal)-atmost(nums,goal-1)

