class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for char in s:
            if char=="]":
                temp=[]
                while stack[-1]!="[":
                    temp.append(stack.pop())
                stack.pop()
                n=""
                while stack and stack[-1].isdigit():
                    n+=stack.pop()
                n=int(n[::-1])
                temp.reverse()
                temp="".join(temp)
                stack.append(temp*n)
            else:
                stack.append(char)
        return "".join(stack)

        
        