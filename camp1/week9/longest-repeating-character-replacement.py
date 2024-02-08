class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        dic={}
        _max=0
        while right <len(s):
            dic[s[right]]=dic.get(s[right],0) +1
            window=right-left+1
            if window - max(dic.values()) <= k:
                 _max=max(_max,sum(dic.values()))
            else:
                dic[s[left]]-= 1
                if not dic[s[left]]:
                    del dic[s[left]]
                left+=1
            right+=1
        return _max
        