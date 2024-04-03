class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions={1:[(0,-1),(0,1)],2:[(1,0),(-1,0)],
        3:[(0,-1),(1,0)],4:[(0,1),(1,0)],5:[(-1,0),(0,-1)],
        6:[(0,1),(-1,0)]
        }
        visited=set()
        def inbound(r,c):
            return 0<=r<len(grid) and 0<=c<len(grid[0])
        def dfs(r,c):
            if r==len(grid)-1 and c==len(grid[0])-1:
                return True
            visited.add((r,c))
            for dr,dc in directions[grid[r][c]]:
                new_row=dr+r
                new_col=dc+c
                if not inbound(new_row,new_col):
                    continue
                if (new_row,new_col) not in visited and (-dr,-dc) in directions[grid[new_row][new_col]]:
                    found=dfs(new_row,new_col)
                    if found:
                        return True
            return False
        return dfs(0,0)

        