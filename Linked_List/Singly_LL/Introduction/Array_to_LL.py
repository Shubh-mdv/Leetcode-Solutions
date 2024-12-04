# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def constructLL(self, arr):
        n = len(arr)
        new_head = Node(arr[0])
        current_node = new_head
        for i in range(1, n):
            new_node = Node(arr[i])
            current_node.next = new_node
            current_node = new_node
        return new_head


arr = [1, 2, 3, 4, 5]
obj = Solution()
print(obj.constructLL(arr))
