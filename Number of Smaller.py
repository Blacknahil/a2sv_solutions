n,m=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
a=0
l=[]
for i in range(m):
    while a<n and arr2[i]> arr1[a]:
        a+=1
    l.append(a)
for i in l:
    print(i,end=" ")
