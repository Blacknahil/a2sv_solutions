class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        N=1e9 + 7
        prefix=[0]* (len(nums) + 1)
        for start, end in requests:
            prefix[start]+=1
            prefix[end+1]-=1
        prefix=prefix[:-1]
        for i in range(1,len(nums)):
            prefix[i]+=prefix[i-1]
        prefix.sort(reverse=True)
        nums.sort(reverse=True)
        ans=0
        for i in range(len(nums)):
            if prefix[i]==0:
                break
            ans+=nums[i] * prefix[i]
        return int(ans % N)