class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans=0
        left=0
        right=len(cardPoints)-k-1
        running_sum=[0]
        for i,points in enumerate(cardPoints):
            running_sum.append(running_sum[-1] + points)
        while right<len(cardPoints):
            cur_sum=running_sum[right+1] -running_sum[left]
            ans=max(ans,running_sum[-1] - cur_sum)
            right+=1
            left+=1
        return ans
        