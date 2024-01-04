class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans=0
        dic={}
        for num in (nums):
            if k-num in dic and dic[k-num] > 0:
                ans+=1
                dic[k-num]-=1
            else:
                dic[num]=dic.get(num,0)+1
        return ans
        