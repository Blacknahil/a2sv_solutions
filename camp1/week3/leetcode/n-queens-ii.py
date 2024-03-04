class Solution:
    def totalNQueens(self, n: int) -> int:
        posDiag=set()
        negDiag=set()
            
        count=0
   
        def backtrack(row,columns):
            nonlocal count
            if row==n:
                count+=1
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

        return count