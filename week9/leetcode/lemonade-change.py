class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives=0
        tens=0
        for bill in bills:
            if bill==5:
                fives+=1
            elif bill==10:
                if fives==0:
                    return False
                fives-=1
                tens+=1
            else:
                while bill>5:
                    if tens and bill>=15:
                        tens-=1
                        bill-=10
                    elif fives and bill>=10:
                        fives-=1
                        bill-=5
                    else:
                        return False
        return True
        