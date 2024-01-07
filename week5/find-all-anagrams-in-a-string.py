class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        comparator=defaultdict(int)
        k=len(p)
        for char in p:
            comparator[char]+=1
        left=0
        counts=[]
        cur=defaultdict(int)
        for right in range(len(s)):
            cur[s[right]]+=1
            if right-left+1==k:
                if cur==comparator:
                    counts.append(left)
                cur[s[left]]-=1
                if cur[s[left]]==0:
                    del cur[s[left]]
                left+=1
            
        return counts

                

        


        