class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums=sorted(nums)
        dic={}
        for i,num in enumerate(sorted_nums):
            if not num in dic:
                dic[num]=i
        ans=[]
        for num in nums:
            ans.append(dic[num])
        return ans
        