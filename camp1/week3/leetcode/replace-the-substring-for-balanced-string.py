class Solution:
    def balancedString(self, s: str) -> int:
        dic=Counter(s)
        left=0
        n=len(s)
        _min=float("inf")
        for right in range(n):
            dic[s[right]]-=1
            while left<n and max(dic.values())<=n//4:
                # print("left",left,"right",right,"dic",dic)
                _min=min(right-left+1,_min)
                dic[s[left]]+=1
                left+=1
        if _min==float("inf"):
            return 0
        return _min

        