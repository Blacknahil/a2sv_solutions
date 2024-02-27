class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        stack=[]
        for i in range(len(nums2)-1,-1,-1):
            while stack and nums2[i]>=stack[-1]:
                stack.pop()
            if stack:
                dic[nums2[i]]=stack[-1]
            else:
                dic[nums2[i]]=-1
            stack.append(nums2[i])
        ans=[]
        for num in nums1:
            ans.append(dic[num])
        return ans

                