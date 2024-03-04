class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        posDiag=set()
        negDiag=set()
            
        ans=[]

        def change(arr):
            state = [["." for _ in range(n)] for _ in range(n)]
            for r, c in enumerate(arr):
                state[r][c] = "Q"
            ans.append(["".join(row) for row in state])

        
        def backtrack(row,columns):
            if row==n:
                change(columns)
                return
            for col in range(n):
                if col in columns or (row+col) in posDiag or (row-col) in negDiag:
                    continue
                columns.append(col)
                posDiag.add(col+row)
                negDiag.add(row-col)
                backtrack(row+1,columns)
                columns.pop()
                posDiag.remove(col+row)
                negDiag.remove(row-col)
        backtrack(0,[])

        return ans