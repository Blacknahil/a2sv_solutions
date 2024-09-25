class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n=0
        for trip in trips:
            n=max(n,trip[2])
        arr=[0]*(n+1)
        for numP,start,to in trips:
            arr[start]+=numP
            arr[to]-=numP
        rs=0
        for numP in arr:
            rs+=numP
            if rs>capacity:
                return False
        return True

        