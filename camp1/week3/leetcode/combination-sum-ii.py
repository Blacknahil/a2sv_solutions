class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=set()
        visited=set()
        candidates.sort()
        def backtrack(cur_arr,idx,summ):
            if summ==target:
                ans.add(tuple(cur_arr[:]))
                return
            if idx>=len(candidates):
                return
            if summ + candidates[idx]>target:
                return
            if tuple(cur_arr) in visited:
                return 
            cur_arr.append(candidates[idx])
            summ+=candidates[idx]
            backtrack(cur_arr,idx+1,summ)
            visited.add(tuple(cur_arr))
            summ-=candidates[idx]
            cur_arr.pop()
            backtrack(cur_arr,idx+1,summ)
            visited.add(tuple(cur_arr))
        backtrack([],0,0)
        return ans
            