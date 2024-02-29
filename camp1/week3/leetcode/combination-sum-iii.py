class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]

        def backtrack(idx,cur_sum,cur_arr):
            if len(cur_arr)==k:
                print(cur_arr)
                if cur_sum==n:
                    ans.append(cur_arr[:])
                return

            if cur_sum>n or idx>9:
                return

 
            cur_arr.append(idx)
            cur_sum+=idx

            backtrack(idx+1,cur_sum,cur_arr)

            cur_sum-=idx
            cur_arr.pop()
            backtrack(idx+1,cur_sum,cur_arr)
        backtrack(1,0,[])
        return ans
        