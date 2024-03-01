class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic_base=Counter(t)
        _min=s+"n"
        left=0
        dic_flex=defaultdict(int)
        required=len(dic_base)
        formed=0
        for right in range(len(s)):
            dic_flex[s[right]]+=1
            if s[right] in dic_base and dic_flex[s[right]]==dic_base[s[right]]:
                formed+=1
            while  left<= right and formed==required:
                _min=min(_min,s[left:right+1],key=len)
                dic_flex[s[left]]-=1
                if s[left] in dic_base and dic_flex[s[left]]<dic_base[s[left]]:
                    formed-=1
                left+=1
        if _min==s+"n":
            return ""
        return _min
               