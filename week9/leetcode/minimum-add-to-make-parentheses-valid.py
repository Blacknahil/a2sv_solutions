class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened=0
        invalid=0
        for par in s:
            if par=="(":
                opened+=1
            elif par==")" and opened:
                opened-=1
            else:
                invalid+=1
        return opened + invalid
        