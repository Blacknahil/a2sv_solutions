class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        index= {}
        for idx, num in enumerate(sorted(nums)):
            index.setdefault(num, idx)
        return [index[num] for num in nums]
