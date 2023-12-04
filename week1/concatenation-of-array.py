class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr=nums
        arr.extend(nums)
        return arr
        