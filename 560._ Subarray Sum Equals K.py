class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix={ 0:1 }
        sub_arrays=0
        cur_sum=0
        for i in nums:
            cur_sum+=i
            diff=cur_sum-k
            if diff in prefix:
                sub_arrays += prefix[diff]
            prefix[cur_sum] = 1 + prefix.get(cur_sum,0)
        return sub_arrays
