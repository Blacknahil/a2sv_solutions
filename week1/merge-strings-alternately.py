class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1=0
        pointer2=0
        ans=""
        while pointer1 < len(word1) and pointer2 <len(word2):
            ans+=word1[pointer1]
            ans+=word2[pointer2]
            pointer1+=1
            pointer2+=1
        if pointer1 < len(word1):
            ans=ans + word1[pointer1:]
        if pointer2 < len(word2):
            ans = ans + word2[pointer2:]
        return ans
        