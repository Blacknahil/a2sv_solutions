class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance=defaultdict()
        for i,point in enumerate(points):
            distance[(point[0],point[1])]=(point[0]**2 ) + (point[1] **2)
        points.sort(key=lambda arr:distance[tuple(arr)])
        return points[:k]
        