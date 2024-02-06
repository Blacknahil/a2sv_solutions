class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix=[]
        runningSum=0
        for num in nums:
            runningSum+=num
            prefix.append(runningSum)
        return prefix