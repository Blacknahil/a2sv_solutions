class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        end=points[0][1]
        count=1
        for point in points:
            if end>=point[0]:
                end=min(end,point[1])
            else:
                count+=1
                end=point[1]
        return count
        