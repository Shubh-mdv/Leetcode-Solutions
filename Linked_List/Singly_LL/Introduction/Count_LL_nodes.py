# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        count = 0
        if head is None:
            return 0
        current_node = head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count
