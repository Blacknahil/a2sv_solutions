class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        max_sum=0

        # def a function that calculates the sum for seven numbers: given r and c
        def sum_up(r,c):
            _sum=grid[r][c] + grid[r][c+1] + grid[r][c+2]
            _sum+=grid[r+1][c+1]
            _sum+=grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2]
            return _sum

        # valid row number that is if r + 2 <row else: break the whole loop

        for r in range(rows):
            if r+2 >= rows:
                break
            # valif col number -- c+2 <col else: break the col loop.
            for c in range(cols):
                if c+2>=cols:
                    break
                cur_sum=sum_up(r,c)
                max_sum=max(max_sum,cur_sum)
        return max_sum



        