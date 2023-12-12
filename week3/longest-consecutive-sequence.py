class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic={}
        for num in nums:
            dic[num]=num+1
        _max=0
        visited={}
        def count_vals(num):
            if num in visited:
                return visited[num] 
            else:
                if dic[num] in dic:
                    x=1 + count_vals(dic[num])
                    visited[num]=x
                    return x
                else:
                    return 1


        for num in nums:
            count=count_vals(num)
            _max=max(_max,count)
        return _max

        