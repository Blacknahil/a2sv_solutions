class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix=[0]
        ans=[]
        n=len(nums)
        for num in nums:
            prefix.append(prefix[-1] + num)
        for i in range(len(nums)):
            left=(nums[i] * i)- prefix[i]
            right=prefix[n]-prefix[i] - (nums[i]*(n-i))
            ans.append(left+right)
        return ans

        