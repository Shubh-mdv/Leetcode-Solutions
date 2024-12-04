class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    # Function to insert a node at the end of the linked list.
    def insertAtEnd(self, head, x):
        new_node = Node(x)
        if head is None:
            return new_node
        current_node = head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
        return head
