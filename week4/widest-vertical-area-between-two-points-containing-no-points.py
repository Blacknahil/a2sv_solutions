class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        max_width=0
        right=1
        while right<len(points):
            max_width=max(max_width,points[right][0]-points[right-1][0])
            right+=1
        return max_width
        