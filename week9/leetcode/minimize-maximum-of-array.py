class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        _max=nums[0]
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            _max=max(_max,math.ceil(total/(i+1)))
        return _max