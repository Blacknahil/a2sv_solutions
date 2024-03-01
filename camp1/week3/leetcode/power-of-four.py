class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        p=0
        while (4**p)<=n:
            if (4**p)==n:
                return True
            p+=1
        return False
        
        