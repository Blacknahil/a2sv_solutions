class Solution:
    def isValid(self, s: str) -> bool:
        dic={")":"(","]":"[","}":"{"}
        stack=[]
        for paren in s:
            if paren in dic.keys():
                if not stack:
                    return False
                    #if the top of the stack is not the pair of the cur paren
                if stack[-1]!=dic[paren]:
                    return False
                stack.pop()
            else:
                stack.append(paren)
        if not stack:
            return True
        return False
        