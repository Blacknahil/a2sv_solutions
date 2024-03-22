class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i=0
        while i<len(nums):
            correct=nums[i]
            if correct==len(nums):
                correct-=1
                nums[correct],nums[i]=nums[i],nums[correct]
                i+=1
            elif correct!=i:
                nums[correct],nums[i]=nums[i],nums[correct]
            else:
                i+=1
        for i,num in enumerate(nums):
            if i!=num:
                return i
        return i+1
        
        