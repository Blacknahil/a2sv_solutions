class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:

        nex=nums[-1]
        pt=len(nums)-2
        steps=0
        if pt>0:
            cur=nums[pt]
        while 0<=pt<len(nums):
            cur=nums[pt]
            if cur>nex:
                spaces=math.ceil(cur/nex)
                steps+=(spaces-1)
                nex=cur//spaces
            else:
                nex=cur
            pt-=1
        return steps
                    




