class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def segregate(self, head):
        count0 = 0
        count1 = 0
        count2 = 0
        current = head
        while current:
            if current.data == 0:
                count0 += 1
            elif current.data == 1:
                count1 += 1
            else:
                count2 += 1
            current = current.next
        current = head
        while current:
            if count0 > 0:
                current.data = 0
                count0 -= 1
                current = current.next
            elif count1 > 0:
                current.data = 1
                count1 -= 1
                current = current.next
            else:
                current.data = 2
                current = current.next
        return head
