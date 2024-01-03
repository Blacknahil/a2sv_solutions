class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid=[[0 for _ in range(n)] for _ in range(m)]
        guarded=set()
        # make the walls
        for r,c in walls:
            grid[r][c]="w"
            # guarded.add(tuple([r,c]))
        for r,c in guards:
            grid[r][c]="g"
        # observe and make it 1 
        for guard in guards:
            #move right
            r,c=guard[0],guard[1] + 1
            while c<n and (grid[r][c] not in ["g","w"]):
                grid[r][c]=1
                guarded.add(tuple([r,c]))
                c+=1
            #move down
            r,c=guard[0]+1,guard[1]
            while r<m and (grid[r][c] not in ["g","w"]):
                grid[r][c]=1
                guarded.add(tuple([r,c]))
                r+=1
            #move up
            r,c=guard[0]-1,guard[1]
            while r>=0 and (grid[r][c] not in ["g","w"]):
                grid[r][c]=1
                guarded.add(tuple([r,c]))
                r-=1
            #move left
            r,c=guard[0],guard[1]-1
            while c>=0 and (grid[r][c] not in ["g","w"]):
                grid[r][c]=1
                guarded.add(tuple([r,c]))
                c-=1
        print(len(guarded))
        # count the zeros and this are the unoccupied and unguarded
        return (m*n)-len(guarded) - len(walls) - len(guards)
        