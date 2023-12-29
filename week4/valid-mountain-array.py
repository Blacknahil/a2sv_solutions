class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        incre=0
        while incre < len(arr)-1:
            if arr[incre] < arr[incre+1]:
                incre+=1
            else:
                break
        decre=len(arr)-1
        while decre >0:
            if arr[decre-1] > arr[decre]:
                decre-=1
            else:
                break
        if decre ==incre and decre !=0 and decre !=len(arr)-1:
            return True
        return False



        