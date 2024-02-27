class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recurse(n,x):
            if n==0:return 1
            if n==1:return x
            if x==0:return 0
            cur=recurse(n//2,x*x)
            if n%2!=0:return x*cur 
            else:return cur

        ans=recurse(abs(n),x)
        if n<0:
            return 1/ans
        return ans
        