class Solution:
    def maxConsecutiveAnswers(self, key: str, k: int) -> int:
        _max=0
        left=0
        right=0
        t_count,f_count=0,0
        while right<len(key):
            if key[right]=='T':
                t_count+=1
            else:
                f_count+=1
            while min(t_count,f_count) >k:
                if key[left]=="T":
                    t_count-=1
                else:
                    f_count-=1
                left+=1
            _max=max(_max,right-left+1)
            right+=1
        return _max
        
