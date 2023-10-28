class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = []
        for numpsg, start, end in trips:
            passengers.append([start, numpsg])
            passengers.append([end, -numpsg])

        passengers.sort()
        total = 0
        for i, numOfpasg in passengers:
            total += numOfpasg
            if total > capacity:
                return False
        return True