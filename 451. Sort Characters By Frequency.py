class Solution:
    def frequencySort(self, s: str) -> str:
        dic=collections.Counter(s)
        ans=sorted(dic,key=lambda item: dic[item], reverse=True)
        ans_str=''
        for i in ans:
            ans_str+=str(i*dic[i])
        return ans_str
