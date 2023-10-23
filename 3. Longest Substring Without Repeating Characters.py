class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        end=0
        _max=0
        while end<len(s):
            sub=s[start:end+1]
            if len(sub)==len(set(sub)):
                _max=max(_max,len(sub))
                end+=1
            else :
                start+=1
        return _max
