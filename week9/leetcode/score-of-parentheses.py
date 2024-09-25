class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        for paren in s:
            if paren==")":
                if stack[-1]==0:
                    stack.pop()
                    stack.append(1)
                    continue
                cur=0
                while stack[-1]!=0:
                    cur+=stack.pop()
                stack.pop()
                stack.append(2*cur)
            else:
                stack.append(0)
        return sum(stack)