t=int(input())
for _ in range(t):
    final_s=input()
    left=0
    right=len(final_s)-1
    l=len(final_s)
    while right>=left:
        if final_s[left] !=final_s[right] and left !=right:
            left+=1
            right-=1
            l-=2
        else:
            break
    print(l)
            