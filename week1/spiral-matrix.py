class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dxn="right"
        arr=[]
        m,n=len(matrix),len(matrix[0])
        matrix_length=m*n
        r_start=0
        r_end=m
        c_start=0
        c_end=n
        r,c=0,0
        while len(arr) <matrix_length:
            if dxn=="right":
                while c<c_end:
                    arr.append(matrix[r][c])
                    c+=1
                c-=1
                r+=1
                r_start+=1
                dxn="down"
            elif dxn=="down":
                while r<r_end:
                    arr.append(matrix[r][c])
                    r+=1
                r-=1
                c-=1
                c_end-=1
                dxn="left"
            elif dxn=="left":
                while c>=c_start:
                    arr.append(matrix[r][c])
                    c-=1
                r_end-=1
                c+=1
                r-=1
                dxn="up"
            elif dxn=="up":
                while r>=r_start:
                    arr.append(matrix[r][c])
                    r-=1
                r+=1
                c_start+=1
                c+=1
                dxn="right"
        return arr

            
            
        