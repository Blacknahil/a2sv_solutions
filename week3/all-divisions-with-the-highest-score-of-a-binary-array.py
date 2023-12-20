class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        # [0,0,1,0]
        #          ^
        # zeros=3
        # ones=0
        # 1 
        # 2
        # 3
        # 2
        # 3
        # dont forget to append the last checking after n it should be n+1 
        ones=nums.count(1)
        score=[]
        zeros=0
        for i in range(len(nums)):
            score.append(ones + zeros)
            if nums[i]==0:
                zeros+=1
            else:
                ones-=1
        score.append(ones+ zeros)
        ans=[]
        _max=max(score)
        for i in range(len(score)):
            if _max==score[i]:
                ans.append(i)
        return ans



        