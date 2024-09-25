n,m=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))

p1,p2=0,0
c=[]

while  p1<n and p2 <m:
    if arr1[p1]< arr2[p2]:
        c.append(arr1[p1])
        p1+=1
    else:
        c.append(arr2[p2])
        p2+=1
if p1<n:
    c.extend(arr1[p1:])
elif p2<m:
    c.extend(arr2[p2:])
        
for i in c:
    print(i,end=" ")
