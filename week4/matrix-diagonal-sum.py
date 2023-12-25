class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        _sum=0
        n=len(mat)
        for r in range(n):
            _sum+=mat[r][r]
            if r!=n-r-1:
                _sum+=mat[r][n-r-1]
        return _sum

        