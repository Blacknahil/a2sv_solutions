class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count=[0]*3
        for i in nums:
            count[i]+=1
        pointer=0
        for i in range(len(count)):
            while count[i] >0:
                nums[pointer]=i
                count[i]-=1
                pointer+=1


       
