class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=set()
        def backtrack(cur_arr,summ):
            if summ>target:
                return
            if summ==target:
                ans.add(tuple(sorted(cur_arr)))
                return 
            for i in range(len(candidates)):
                if candidates[i]+summ<=target:
                        cur_arr.append(candidates[i])
                        backtrack(cur_arr,summ+candidates[i])
                        cur_arr.pop()
        backtrack([],0)
        return ans