class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.dict[key]
        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
     
        if left == 0:
            return ''
        
        return values[left-1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)