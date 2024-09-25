class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        cur=target
        steps=0
        while cur >1:
            if maxDoubles:
                if cur %2==0:
                    cur=cur//2
                    steps+=1
                    maxDoubles-=1
                else:
                    steps+=1
                    cur-=1
            else:
                steps+=(cur-1)
                cur=1
        return steps

