class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n==1:
            return 0
        elif n%2==0:
            return n//2
        return n
        