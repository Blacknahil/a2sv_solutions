class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows=len(mat)
        columns=len(mat[0])
        elements=0
        r=0
        c=0
        dxn="up"
        arr=[]
        while len(arr)< rows * columns:
            if dxn=="up":
                while r >= 0 and c < columns:
                    arr.append(mat[r][c])
                    r-=1
                    c+=1
                dxn="down"
                r+=1
                if c==columns:
                    c-=1
                    r+=1
                
            elif dxn=="down":
                while r<rows and c >=0:
                    arr.append(mat[r][c])
                    r+=1
                    c-=1
                dxn="up"
                c+=1
                if r==rows:
                    r-=1
                    c+=1
        return arr
                


            


        