class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def recurse(pos,total):
            if total==1:
                return 0
            half=total//2
            if pos>half:
                return 1-recurse(pos-half,total-half)
            return recurse(pos,total-half)
        return recurse(k,2**(n-1))
