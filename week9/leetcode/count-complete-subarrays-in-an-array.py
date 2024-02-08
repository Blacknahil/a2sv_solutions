class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        complete=0
        left=0
        unique=len(set(nums))
        dic={}
        for right in range(len(nums)):
            dic[nums[right]]=dic.get(nums[right],0)+1
            while len(dic.keys())>=unique:
                complete+=(len(nums)-right)
                dic[nums[left]]-=1
                if dic[nums[left]]==0:
                    del dic[nums[left]]
                left+=1
        return complete

        