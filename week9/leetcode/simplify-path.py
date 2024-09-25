class Solution:
    def simplifyPath(self, path: str) -> str:
        ls=path.split("/")
        stack=[]
        for char in ls:
            if char==".":
                continue
            elif char=="..":
                if stack:
                    stack.pop()
            elif char:
                stack.append(char)
        return "/"+"/".join(stack)

        