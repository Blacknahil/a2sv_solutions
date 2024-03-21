class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda num:abs(num-x))
        ans=arr[:k]
        return sorted(ans)