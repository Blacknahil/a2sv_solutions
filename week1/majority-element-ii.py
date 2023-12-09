class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic={}
        min_freq=len(nums) //3
        ans=set()
        for num in nums:
            dic[num]=dic.get(num,0) +1
            if dic[num] >min_freq:
                ans.add(num)
        return ans
        