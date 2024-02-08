class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running=[0]
        for num in nums:
            running.append(num+ running[-1])
        return running[1:]
