class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count=0
        expected_sum=0
        cur_sum=0
        for i in range(len(flips)):
            cur_sum+=flips[i]
            expected_sum+=(i+1)
            if cur_sum==expected_sum:
                count+=1
        return count
            

        