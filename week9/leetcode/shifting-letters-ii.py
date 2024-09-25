class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        changes=[0] * (n+1)
        for start,end,dxn in shifts:
            if dxn==0:
                changes[start]-=1
                changes[end+1]+=1
            else:
                changes[start]+=1
                changes[end+1]-=1
        for i in range(1,n+1):
            changes[i]+=changes[i-1]
        s=list(s)
        for i in range(n):
            shift=changes[i]
            s[i]=chr( ( (ord (s[i])-97+shift) %26) +97)
        return "".join(s)
