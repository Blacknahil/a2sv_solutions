class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        moved=0
        for i in spaces:
            s=s[:i+moved] + " " + s[i+moved:]
            moved+=1
        return s
        