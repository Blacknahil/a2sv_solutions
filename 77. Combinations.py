class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        
        def back_track(start,lst):
            if len(lst)==k:
                ans.append(lst.copy())
                return
            for i in range(start,n+1):
                lst.append(i)
                back_track(i+1,lst)
                lst.pop()
            
            
        back_track(1,[])
        return ans
