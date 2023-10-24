import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers=[0] * 10001
        for t in trips:
            pas,start,end=t
            passengers[start] +=pas
            passengers[end] -=pas
        prefix=0
        for i in range(len(passengers)):
            prefix+=passengers[i]
            passengers[i]=prefix
            if prefix > capacity:
                return False
        return True
