class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        count=0
        def checker(left,right):
            nonlocal count
            while left>=0 and right<n:
                if s[left]==s[right]:
                    count+=1
                    left-=1
                    right+=1
                else:
                    break
        for i in range(n):
            checker(i,i)
            checker(i,i+1)
        return count
        
            
            

            
        