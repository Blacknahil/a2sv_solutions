class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q=deque()
        ans=[]
        for i in range(len(temperatures)-1,-1,-1):
            if not q:
                ans.append(0)
            elif q[-1][0]>temperatures[i]:
                ans.append(1)
            else:
                while q and q[-1][0]<=temperatures[i]:
                    q.pop()
                if q:
                    ans.append(q[-1][1]-i)
                else:
                    ans.append(0)
            q.append([temperatures[i],i])
        ans.reverse()
        return ans

        