class Solution:
    def countGoodNumbers(self, n: int) -> int:
            mod= ((10**9) +7)
            count=1
            if n%2==0:
                half=n//2
                count *=pow(5,half,mod)
                count %= mod
                count*=pow(4,half,mod)
            else:
                half=n//2
                count*=pow(5,half+1,mod)
                count %= mod
                count*=pow(4,half,mod)
            return count %mod
        
        