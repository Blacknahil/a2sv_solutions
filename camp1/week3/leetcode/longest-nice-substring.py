class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        unique=set(s)

        for i,char in enumerate(s):
            if char.swapcase() not in unique:
                return max(self.longestNiceSubstring(s[:i]),self.longestNiceSubstring(s[i+1:]),key=len)
        return s