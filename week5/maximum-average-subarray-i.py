class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum=0
        max_sum=float("-inf")
        left=0
        for right in range(len(nums)):
            cur_sum+=nums[right]
            if right-left+1==k:
                 max_sum=max(max_sum,cur_sum)
                 cur_sum-=nums[left]
                 left+=1
        return max_sum/k
        