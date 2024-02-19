class LinkedList():
    def __init__(self, val = '', next = None, prev = None):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.node = LinkedList(homepage)
        self.curr = self.node
        

    def visit(self, url: str) -> None:
        node = LinkedList(url)
        self.curr.next = node
        node.prev = self.curr
        self.curr = self.curr.next
        

    def back(self, steps: int) -> str:
        while steps and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        while steps and self.curr.next:
            self.curr = self.curr.next
            steps -= 1

        return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)