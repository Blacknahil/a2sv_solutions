n,k=map(int,input().split())
arr=list(map(int,input().split()))
next_round=0
_min=arr[k-1]
for point in arr:
    if point < _min:
        break
    elif point !=0:
        next_round+=1
    
print(next_round)
    