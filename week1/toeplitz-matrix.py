class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for r in range(len(matrix)-1):
            for c in range(len(matrix[0])-1):
                #condition
                if matrix[r][c] != matrix[r+1][c+1]:
                    return False
        return True

        