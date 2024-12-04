class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def segregate(self, head):
        zero = Node(0)
        one = Node(1)
        two = Node(2)
        zeroH = zero
        oneH = one
        twoH = two
        current = head
        while current:
            if current.data == 0:
                zero.next = current
                zero = zero.next
            elif current.data == 1:
                one.next = current
                one = one.next
            else:
                two.next = current
                two = two.next
            current = current.next
        if oneH.next is not None:
            zero.next = oneH.next
        else:
            zero.next = twoH.next
        one.next = twoH.next
        two.next = None

        return zeroH.next
