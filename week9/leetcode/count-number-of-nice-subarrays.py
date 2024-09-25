class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dic=defaultdict(int)
        dic[0]=1
        odd_prefix=0
        count=0
        for num in nums:
            if num%2!=0:
                odd_prefix+=1
            if odd_prefix-k in dic:
                count+=dic[odd_prefix-k]
            dic[odd_prefix]+=1
        return count
