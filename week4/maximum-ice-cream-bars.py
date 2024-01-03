class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        for cost in costs:
            if cost<=coins:
                coins-=cost
                count+=1
            else:
                break
        return count
        