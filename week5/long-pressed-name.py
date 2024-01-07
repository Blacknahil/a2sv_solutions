class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        t=0
        n=0
        if name[0] != typed[0]:
            return False
        while n< len(name) and t < len(typed):
            if typed[t] ==name[n]:
                n+=1
                t+=1
            elif typed[t]==name[n-1]:
                t+=1
            else:
                return False
            if t==len(typed) and n !=len(name):
                return False
        if t !=len(typed):
            while t < len(typed):
                if typed[t] != name[n-1]:
                    return False
                t+=1
        return True

        