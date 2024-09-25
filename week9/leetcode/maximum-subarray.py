class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        chopped=0
        maxSum=float("-inf")
        prefix=0
        for num in nums:
            prefix+=num
            maxSum=max(maxSum,prefix-chopped)
            chopped=min(chopped,prefix)
        return maxSum
        