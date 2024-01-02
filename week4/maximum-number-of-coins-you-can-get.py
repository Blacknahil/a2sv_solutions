class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        me=len(piles)-2
        alice=len(piles)-1
        bob=0
        total=0
        while bob<len(piles)//3:
            total+=piles[me]
            me-=2
            alice-=2
            bob+=1
        return total

        