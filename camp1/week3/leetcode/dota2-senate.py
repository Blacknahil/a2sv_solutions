class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad=deque([])
        dire=deque([])
        banned_dire=0
        banned_rad=0
        for i,char in enumerate(senate):
            if char=="R":
                rad.append(i)
            else:
                 dire.append(i)
        le=len(senate)
        while dire and rad:
            d=dire.popleft()
            r=rad.popleft()
            if d>r:
               rad.append(r+le)
            else:
                dire.append(d+le)
        if rad:
            return "Radiant"
        return "Dire"

        