class Solution:
    def totalMoney(self, n: int) -> int:
        mon=1
        count=0
        while n>0:
            if n>=7:
                days=7
                n-=7
            else:
                days=n
                n=0
            for i in range(0,days):
                count+=mon+i
            mon+=1
        return count
        