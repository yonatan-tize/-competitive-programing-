class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.stream = [0] * n
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey-1] = value
        if idKey-1 == self.pointer:
            while self.pointer < self.n and self.stream[self.pointer] != 0:
                self.pointer += 1 
        return self.stream[idKey-1:self.pointer]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)