class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans=[]
        dic={2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],
        5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],
        9:["w","x","y","z"]}
        def dfs(idx,cur):
            if len(cur)==len(digits):
                st=cur[:]
                if not st:
                    return 
                ans.append("".join(st))
                return 
            key=int(digits[idx])
            for altern in dic[key]:
                cur.append(altern)
                dfs(idx+1,cur)
                cur.pop()
        dfs(0,[])
        return ans
        