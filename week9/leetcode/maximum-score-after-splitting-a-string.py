class Solution:
    def maxScore(self, s: str) -> int:
        ones=0
        max_sum=0
        zeros=0
        for char in s:
            if char=="1":
                ones+=1
        for i in range(len(s)-1):
            if s[i]=="0":
                zeros+=1
            else:
                ones-=1
            max_sum=max(max_sum,zeros+ones)
        return max_sum
        