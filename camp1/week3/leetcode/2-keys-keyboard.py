class Solution:
    def minSteps(self, n: int) -> int:
        cur=1
        count=0
        last=1
        while cur<n:
            if n%cur==0:
                count+=2
                last=cur
                cur*=2
                # print("cur",cur,"count",count,"last",last)
            else:
                count+=1
                cur+=last
                # print("cur",cur,"count",count,"last",last)
        # print(last,cur,count)
        return count





        