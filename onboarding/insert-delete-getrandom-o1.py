class RandomizedSet:

    def __init__(self):
        self.store = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val not in self.store:
            self.store[val] = len(self.nums)
            self.nums.append(val)
            return True
        else:
            # self.store[val] = len(self.nums)
            # self.nums.append(val)
            return False
    def remove(self, val: int) -> bool:
        if val in self.store:
            index = self.store[val]
            n = self.nums[-1]
            self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
            self.nums.pop()
            self.store[n] = index 
            del self.store[val] 
            return True
        else:
            return False

    def getRandom(self) -> int:
        r = random.choice(self.nums)
        return r


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()