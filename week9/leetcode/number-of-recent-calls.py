class RecentCounter:

    def __init__(self):
        self.pings=deque()
        self.count=0
        

    def ping(self, t: int) -> int:
        self.pings.append(t)
        self.count+=1
        while t-self.pings[0]>3000:
            self.count-=1
            self.pings.popleft()
        return self.count
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)