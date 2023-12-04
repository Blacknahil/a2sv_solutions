class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _max=0
        left=0
        right=0
        while right < len(nums):
            if nums[right]==0:
                _max=max(_max,right-left)
                left=right+1
            elif right==len(nums)-1:
                _max=max(_max,right-left+1)
            right+=1
        return _max
        