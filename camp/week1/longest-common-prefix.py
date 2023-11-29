class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=[len(word) for word in strs]
        _min=min(l)
        char=0
        if not strs:
            return ""
        ans="" 
        for char in range(_min):
            cur=strs[0][char]
            for word in strs:
                if not word:
                    return ""
                elif word[char] !=cur:
                    return ans
            ans+=strs[0][char]
        return ans


        