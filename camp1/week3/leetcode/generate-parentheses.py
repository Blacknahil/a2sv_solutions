class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]

        def backtrack(opened,close,cur):
            if opened+close>2*n:
                return
            if close>n or opened>n:
                return 
            if close==n and opened==n:
                ans.append("".join(cur[:]))
                return
            cur.append("(")
            backtrack(opened+1,close,cur)
            cur.pop()
            if opened-close>=1:
                cur.append(")")
                backtrack(opened,close+1,cur)
                cur.pop()
        backtrack(0,0,[])
        return ans
        
        