class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True 
        elif n==0:
            return False 
        ans=n
        while ans>=4:
            ans=ans/4
        return True if ans==0 or ans ==1 else False
