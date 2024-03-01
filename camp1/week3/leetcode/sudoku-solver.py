class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dic_col=defaultdict(list)
        dic_row=defaultdict(list)
        dic_part=defaultdict(list)
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                dic_col[c].append(board[r][c])
                dic_row[r].append(board[r][c])
                dic_part[(r//3,c//3)].append(board[r][c])
        count=0
        def backtrack(r,c):
            if r>=9:
                print(board)
                return True
            if c>=9:
                return backtrack(r+1,0)
            if board[r][c]!=".":
                return backtrack(r,c+1)
            # print(r,c)
            for i in range(1,10):
                check=str(i)
                if check in dic_col[c] or check in dic_row[r] or check in dic_part[(r//3,c//3)]:
                    continue
                # print(i)

                dic_col[c].append(check)
                dic_row[r].append(check)
                dic_part[(r//3,c//3)].append(check)
                board[r][c]=check
                if backtrack(r,c+1):
                    return board

                dic_col[c].pop()
                dic_row[r].pop()
                dic_part[(r//3,c//3)].pop()
                board[r][c]="."
            return 
        backtrack(0,0)