class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left,right=0,0
        unique=set()
        max_sum=0
        prefix=[0]
        cur_sum=0
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
        while right<len(nums):
            while nums[right] in unique:
                # if it is no longer unique move the left pointer
                unique.remove(nums[left])
                left+=1
            unique.add(nums[right])
            max_sum=max(max_sum,prefix[right+1]-prefix[left])
            right+=1
        return max_sum

        #instead of using sum everytime we got a unique combinations we could use a prefix sum
        