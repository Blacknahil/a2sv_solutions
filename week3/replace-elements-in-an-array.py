class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic={}
        for i in range(len(nums)):
            dic[nums[i]]=i
        for old_val, new_val in operations:
            nums[dic[old_val]]=new_val
            dic[new_val]=dic[old_val]
        return nums

