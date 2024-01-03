class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)==2:
            return skill[0] * skill[1]
        left=0
        right=len(skill)-1
        skill.sort()
        ans=0
        _sum=skill[left] + skill[right]
        while left<right:
            if skill[left] + skill[right] !=_sum:
                return -1
            ans+=skill[left] * skill[right]
            left+=1
            right-=1
        return ans

        