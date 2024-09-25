class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=0
        dic={0:1}
        count=0
        for num in nums:
            prefix+=num
            if prefix-k in dic:
                count+=dic[prefix-k]
            dic[prefix]=dic.get(prefix,0) +1
        return count
        