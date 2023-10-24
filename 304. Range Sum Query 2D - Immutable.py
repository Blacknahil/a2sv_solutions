class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows=len(matrix)
        cols=len(matrix[0])
        self.prefix_sum=[[0] * (cols +1) for _ in range(rows+1)]
        for r in range(rows):
            row_prefix=0
            for c in range(cols):
                row_prefix+=matrix[r][c]
                above=self.prefix_sum[r][c+1]
                self.prefix_sum[r+1][c+1]=row_prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomright=self.prefix_sum[row2 +1][col2 +1]
        left=self.prefix_sum[row2+1][col1]
        top=self.prefix_sum[row1][col2+1]
        topleft=self.prefix_sum[row1][col1]
        return bottomright - left -top + topleft
     
        

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
