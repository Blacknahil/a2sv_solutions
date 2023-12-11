class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic={}
        for winner,loser in matches:
            if winner in dic:
                dic[winner][0]+=1
            else:
                dic[winner]=[1,0]
            if loser in dic:
                dic[loser][1]+=1
            else:
                dic[loser]=[0,1]
        perfect_wins=[]
        losers1=[]
        for player in dic.keys():
            wins,loses=dic[player][0], dic[player][1]
            if loses==0 and wins!=0:
                perfect_wins.append(player)
            elif loses==1:
                losers1.append(player)
        perfect_wins.sort()
        losers1.sort()
        return perfect_wins,losers1


        