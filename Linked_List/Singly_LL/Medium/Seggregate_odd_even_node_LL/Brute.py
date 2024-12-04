from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        current = head
        while current:
            values.append(current.val)
            if current.next:
                current = current.next.next
            else:
                break
        current = head.next
        while current:
            values.append(current.val)
            if current.next:
                current = current.next.next
            else:
                break
        index = 0
        current = head
        while current:
            current.val = values[index]
            index += 1
            current = current.next
        return head
