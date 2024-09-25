class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        memo={}
        def factorial(n):
            if n in memo:
                return memo[n]
            if n==1 or n==0:
                return 1
            memo[n]=n*factorial(n-1)
            return memo[n]
        ans=[]
        for i in range(0,rowIndex+1):
            value=(factorial(rowIndex)//(factorial(i) * factorial(rowIndex-i)))
            ans.append(value)
        return ans
        