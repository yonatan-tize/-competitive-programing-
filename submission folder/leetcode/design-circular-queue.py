class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = deque(maxlen = k)
        

    def enQueue(self, value: int) -> bool:
        if len(self.queue) < self.size:
            self.queue.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if self.queue:
            self.queue.popleft()
            return True
        return False
        

    def Front(self) -> int:
        if not self.queue:
            return -1
        else:
            return self.queue[0]
        
    def Rear(self) -> int:
        if not self.queue:
            return -1
        else:
            return self.queue[-1]
        
    def isEmpty(self) -> bool:
        if self.queue:
            return False
        return True

    def isFull(self) -> bool:
        return  len(self.queue) == self.size
        

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()