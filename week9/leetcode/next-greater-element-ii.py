class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return [-1]
        stack=[]
        ans=[]
        for i in range(len(nums)-2,-1,-1):
            while stack and stack[-1]<nums[i]:
                stack.pop()
            stack.append(nums[i])
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[i]>=stack[-1]:
                stack.pop()
            if stack:
                ans.append(stack[-1])
            else:
                ans.append(-1)
            stack.append(nums[i])
        ans.reverse()
        return ans