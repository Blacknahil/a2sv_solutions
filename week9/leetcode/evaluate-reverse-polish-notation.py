class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=["+","-","/","*"]
        for token in tokens:
            if not token in operators:
                stack.append(int(token))
            else:
                var1=stack.pop()
                var2=stack.pop()
                if token=="/":
                    ans=math.trunc(var2/var1)
                    stack.append(ans)
                elif token=="-":
                    stack.append(var2-var1)
                elif token=="+":
                    stack.append(var2+var1)
                else:
                    stack.append(var1*var2)
        return stack[-1]
        