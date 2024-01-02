class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for r in range(9):
            check=set()
            for c in range(9):
                if board[r][c] in check:
                    return False
                if board[r][c] !=".":
                    check.add(board[r][c])
        for c in range(9):
            check=set()
            for r in range(9):
                if board[r][c] in check:
                    return False
                if board[r][c] !=".":
                    check.add(board[r][c])
        def cube(row,col):
            backend=[]
            for r in range(row,row+3):
                for c in range(col,col+3) :
                    print(r,c)
                    if board[r][c] in backend:
                        return False
                    if board[r][c] !=".":
                        backend.append(board[r][c])
            return True
        squares=[[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
        for pos in squares:
            if not cube(pos[0],pos[1]):
                return False
        return True   

        # [".",".",".",".",".",".","5",".","."],
        # [".",".",".",".",".",".",".",".","."],
        # [".",".",".",".",".",".",".",".","."],
        # ["9","3",".",".","2",".","4",".","."],
        # [".",".","7",".",".",".","3",".","."],
        # [".",".",".",".",".",".",".",".","."],
        # [".",".",".","3","4",".",".",".","."],
        # [".",".",".",".",".","3",".",".","."],
        # [".",".",".",".",".","5","2",".","."]  
        