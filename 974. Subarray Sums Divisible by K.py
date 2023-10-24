class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic={ 0: 1}
        count=0
        prefix=0
        for num in nums:
            prefix+=num
            reminder = abs(prefix % k)
            if reminder in dic:
                count+=dic[reminder]
                dic[reminder] +=1
            else:
                dic[reminder] = 1
        return count
            
