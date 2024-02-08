class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic=defaultdict(int)
        dic[0]=1
        prefix=0
        count=0
        for right in range(len(nums)):
            prefix+=nums[right]
            r=prefix%k
            count+=dic[r]
            dic[r]+=1
        return count


        