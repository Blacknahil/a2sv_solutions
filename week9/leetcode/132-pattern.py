class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        _min=nums[0]
        for i,num in enumerate(nums):
            while stack and num >stack[-1][0]:
                stack.pop()
            if stack and stack[-1][0]>num and num>stack[-1][1]:
                    return True
            stack.append((num,_min))
            _min=min(_min,num)
        return False
            
            
        