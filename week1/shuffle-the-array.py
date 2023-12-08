class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_arr=[]
        for i in range(n):
            new_arr.append(nums[i])
            new_arr.append(nums[i+n])
        return new_arr
        