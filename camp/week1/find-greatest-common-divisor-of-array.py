class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num=min(nums)
        max_num=max(nums)
        for div in range(min_num,0,-1):
            if max_num % div==0 and min_num %div==0:
                return div

        