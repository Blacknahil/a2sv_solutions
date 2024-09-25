class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penaltyN=[0]
        n=len(customers)
        for char in customers:
            if char=="N":
                penaltyN.append(penaltyN[-1] +1)
            else:
                penaltyN.append(penaltyN[-1])
        penaltyY=[0]*(n+1)
        for i in range(n-1,-1,-1):
            if customers[i]=="Y":
                penaltyY[i]=penaltyY[i+1]+1
            else:
                penaltyY[i]=penaltyY[i+1]
        _min=float("inf")
        _minH=0
        for j in range(n+1):
            if penaltyY[j]+penaltyN[j]<_min:
                _min=penaltyY[j]+penaltyN[j]
                _minH=j

        return _minH

        