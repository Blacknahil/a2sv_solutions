class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt_s1=Counter(s1)
        window=len(s1)
        for i in range(len(s2)-window +1):
            cnt_s2=Counter(s2[i:i+window])
            if cnt_s1==cnt_s2:
                return True
        return False

        