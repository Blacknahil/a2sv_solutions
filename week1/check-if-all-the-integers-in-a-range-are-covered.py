class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        total_range=set()
        for r in ranges:
            for i in range(r[0],r[1]+1):
                total_range.add(i)
        for j in range(left,right+1):
            if j not in total_range:
                return False
        return True
        