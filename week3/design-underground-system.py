class UndergroundSystem:

    def __init__(self):
        self.dic={}
        self.completed=defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.dic[id]=[stationName,t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start=self.dic[id]
        self.completed[(start[0],stationName)].append(abs(start[1]-t))

        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        arr=self.completed[(startStation,endStation)]
        return sum(arr)/len(arr)
        


["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn",
"getAverageTime",
"checkOut",
"getAverageTime"]

[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],
[10,"Waterloo",38],
["Leyton","Waterloo"]]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)