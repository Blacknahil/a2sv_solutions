class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic={}
        for i,char in enumerate(s):
            dic[char]=i
        left=0
        right=0
        ans=[]
        goal=dic[s[left]]
        while right < len(s):
            goal=max(goal,dic[s[right]])
            if right ==goal:
                ans.append(right-left+1)
                left=right+1
            right+=1
            

        return ans
        