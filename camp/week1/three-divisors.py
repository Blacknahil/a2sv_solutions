class Solution:
    def isThree(self, n: int) -> bool:
        count=0
        for div in range(2,n):
            if n%div==0:
                count+=1
            if count>1:
                return False
        if count==1:
            return True
        