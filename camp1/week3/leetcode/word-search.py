class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        col=len(board[0])
        row=len(board)
        visited=defaultdict(bool)
        
        def backtrack(r,c,idx):
            if idx==len(word):
                return True
            if r>=row or r<0 or c>=col or c<0:
                return False

            if visited[(r,c)] or board[r][c] != word[idx]:
                return False
            visited[(r,c)]=True
            if backtrack(r+1,c,idx+1) or backtrack(r,c+1,idx+1): 
                return True
            if backtrack(r-1,c,idx+1) or backtrack(r,c-1,idx+1):
                return True
            visited[(r,c)]=False
            return False
        
        for ir in range(row):
            for jc in range(col):
                if board[ir][jc]==word[0]:
                    if backtrack(ir,jc,0):
                        return True
        return False
      