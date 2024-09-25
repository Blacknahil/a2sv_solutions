class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product=[1]
        n=len(nums)
        suffix_product=[1]
        for num in nums:
            prefix_product.append(prefix_product[-1] * num)
        for i in range(len(nums)-1,-1,-1):
            suffix_product.append(nums[i] * suffix_product[-1])
        for i in range(n):
            nums[i]=prefix_product[i] * suffix_product[n-i-1]
        return nums
        