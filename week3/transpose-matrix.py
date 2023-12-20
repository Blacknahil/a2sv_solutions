class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row=len(matrix)
        col=len(matrix[0])
        # create an array of zeros that have the same size as our answer 
        mat=[[0] * row for _ in range(col)]

        # iterate over the matrix and inverse the indexs and assign values
        for i in range(row):
            for j in range(col):
                mat[j][i]=matrix[i][j]
        return mat
        