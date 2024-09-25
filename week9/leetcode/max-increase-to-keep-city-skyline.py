class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n=len(grid)
        colMax=[]
        added=0
        #finding the maximum in a given row and storing it in an array
        for c in range(n):
            _max=grid[0][c]
            for r in range(n):
                _max=max(_max,grid[r][c])
            colMax.append(_max)
        for r in range(n):
            rowMax=max(grid[r])
            for c in range(n):
                added+=(min(rowMax,colMax[c])-grid[r][c])
        return added
        