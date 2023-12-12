class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,n in enumerate(nums):
            m=target-n
            if m in dic:
                return dic[m],i
            else:
                dic[n]=i
            
        