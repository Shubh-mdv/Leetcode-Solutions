class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def searchKey(self, n, head, key):
        if head is None:
            return False
        current_node = head
        count = 0
        while count < n:
            if current_node.data == key:
                return True
            else:
                current_node = current_node.next
                count += 1
