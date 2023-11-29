class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num=float("inf")
        max_num=0
        for num in nums:
            min_num=min(min_num,num)
            max_num=max(max_num,num)
        
        for div in range(min_num,0,-1):
            if min_num % div==0 and max_num %div==0:
                return div

        [2,5,6,9,10]
        