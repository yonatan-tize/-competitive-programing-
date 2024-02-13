class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        temp = self.head
        while temp and index > 0:
            temp = temp.next
            index -= 1

        if temp:
            return temp.value
        return -1

    def addAtHead(self, val: int) -> None:
        temp = Node(val)
        temp.next = self.head
        self.head = temp

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        temp = self.head
        while temp and temp.next:
            temp = temp.next
        if temp:
            temp.next = node
        else:
            self.head = node

    def addAtIndex(self, index: int, val: int) -> None:
        dummy = Node(1)
        dummy.next = self.head
        temp = dummy

        while temp and index > 0:
            index -= 1
            temp = temp.next

        if not temp:
            return

        newN = Node(val)
        newN.next = temp.next
        temp.next = newN
        self.head = dummy.next

    def deleteAtIndex(self, index: int) -> None:

        dummy = Node(1)
        dummy.next = self.head
        temp = dummy

        while index > 0 and temp:
            index -= 1
            temp = temp.next

        if not temp:
            return

        if  temp.next:
            temp.next = temp.next.next
        self.head = dummy.next


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)