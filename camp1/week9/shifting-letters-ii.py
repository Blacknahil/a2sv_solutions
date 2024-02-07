class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        moves=[0] * (len(s)+1)
        for start,end,dxn in shifts:
            if dxn==0:
                dxn=-1
            moves[start]+=dxn
            moves[end+1]-=dxn
        shift=0
        result = ''
        for i in range(len(s)):
            shift=shift + moves[i]
            result += chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
        return result
        



        