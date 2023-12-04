class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        n=(num-3)/3
        if n==int(n):
            n=int(n)
            return [n,n+1,n+2]
        return []
        