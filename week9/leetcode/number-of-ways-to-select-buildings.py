class Solution:
    def numberOfWays(self, s: str) -> int:
        n=len(s)
        count=0
        ones_after=s.count("1")
        zeros_after=s.count("0")
        zeros_before=0
        ones_before=0
        for i in range(n):
            if s[i]=="1":
                count+=(zeros_before*zeros_after)
                ones_after-=1
                ones_before+=1
            else:
                count+=(ones_before*ones_after)
                zeros_after-=1
                zeros_before+=1
        return count