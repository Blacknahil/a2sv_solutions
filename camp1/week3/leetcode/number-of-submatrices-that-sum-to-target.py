class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows=len(matrix)
        columns=len(matrix[0])
        grid=[[0]*(columns+1)]
        for row in matrix:
            grid.append([0]+row)
        for r in range(1,rows+1):
            for c in range(1,columns+1):
                grid[r][c]+=grid[r-1][c] + grid[r][c-1]-grid[r-1][c-1]
        #till now i was doing the prefix sum by managing not to go out of the index

        count=0
        for r1 in range(rows):
            for r2 in range(r1,rows):
                dic=defaultdict(int)
                dic[0]=1
                for c in range(columns):
                    cur_sum=grid[r2+1][c+1] - grid[r1][c+1]
                    diff=cur_sum-target
                    count+=dic[diff]
                    dic[cur_sum]+=1
        return count
        