class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda arr:arr[0]-arr[1])
        total_cost=0
        n=len(costs)//2
        for i in range(len(costs)):
            if i<n:
                total_cost+=costs[i][0]
            else:
                total_cost+=costs[i][1]
        return total_cost
        
        