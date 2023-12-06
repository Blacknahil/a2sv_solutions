class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        clock,anti_clock=0,0
        cur=start
        n=len(distance)
        while cur !=destination:
            clock+=distance[cur]
            cur=(cur + 1) % n
                
        #going anticlock_wise
        cur=destination
        while cur !=start:
            anti_clock+=distance[cur]
            cur=(cur+1) %n
        return min(clock,anti_clock)
        