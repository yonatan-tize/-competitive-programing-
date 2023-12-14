class FrequencyTracker:

    def __init__(self):
        self.array = defaultdict(int)
        self.frequency = defaultdict(int)

    def add(self, number: int) -> None: #add data to the data structure
        if number in self.array and self.array[number] in self.frequency:
            self.frequency[self.array[number]] -= 1 
        self.array[number] += 1 
        self.frequency[self.array[number]] += 1 

    def deleteOne(self, number: int) -> None: #delete one data if present in the
        if number in self.array and self.array[number] > 0:
            self.frequency[self.array[number]] -= 1 
            self.array[number] -= 1
            self.frequency[self.array[number]] += 1 
        
    def hasFrequency(self, freq: int) -> bool: #if we have value 
        return True if self.frequency[freq] > 0 else False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)