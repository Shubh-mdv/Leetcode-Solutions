class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        pass

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        prev = None
        current = self.head
        count = 0
        while current is not None:
            if count == index:
                new_node = Node(val)
                new_node.next = current
                prev.next = new_node
            else:
                prev = current
                current = current.next
                count += 1

    def deleteAtIndex(self, index: int) -> None:
        pass


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
