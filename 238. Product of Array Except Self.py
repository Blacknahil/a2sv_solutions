class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product=[nums[0]]
        for i in range(1,len(nums)):
            prefix_product.append(prefix_product[-1] * nums[i])
        sufix_product=[nums[-1]]
        for i in range(len(nums)-2,-1,-1):
            sufix_product.append(sufix_product[-1] * nums[i])
        sufix_product.reverse()
        arr=[]
        arr.append(sufix_product[1])
        for i in range(1,len(nums)-1):
            arr.append(sufix_product[i+1]* prefix_product[i-1])
        arr.append(prefix_product[-2])
        return arr
                
