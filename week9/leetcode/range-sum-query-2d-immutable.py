class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows=len(matrix)
        cols=len(matrix[0])
        self.grid=[[0]*(cols+1)]
        for i in range(rows):
            row=[0]+matrix[i]
            self.grid.append(row)
        for r in range(1,rows+1):
            for c in range(1,cols+1):
                self.grid[r][c]+=self.grid[r-1][c] + self.grid[r][c-1]-self.grid[r-1][c-1]



        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total=self.grid[row2+1][col2+1]-self.grid[row2+1][col1]-self.grid[row1][col2+1] + self.grid[row1][col1]
        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)