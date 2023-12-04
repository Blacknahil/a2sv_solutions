class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        visited=[]
        ans=0
        for point in points:
            if visited and point not in visited:
                cur=visited[-1]
                ans+=max(abs(cur[0]-point[0]),abs(cur[1]-point[1]))
            visited.append(point)
        return ans

        