class UndergroundSystem:

    def __init__(self):
        self.start = {}
        self.totalTime = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        name, time = self.start[id]
        w = name.upper() + stationName
        if w not in self.totalTime:
            self.totalTime[w] = [t-time]
        else:
            self.totalTime[w].append(t-time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        a = startStation.upper() + endStation
        nums = self.totalTime[a]
        return sum(nums) / len(nums)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)