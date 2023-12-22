class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        l=len(strs[0])
        count=0
        for i in range(l):
            col_word=''
            for st in strs:
                col_word+=st[i]
            sorted_col=sorted(col_word)
            sorted_col="".join(sorted_col)
            if col_word == sorted_col:
                continue
            else:
                count+=1
        return count
            



        