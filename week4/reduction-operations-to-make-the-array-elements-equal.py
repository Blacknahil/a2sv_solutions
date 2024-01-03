class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        operations=[0]
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                operations.append(operations[-1])
            else:
                operations.append(operations[-1] +1)
        return sum(operations)

        