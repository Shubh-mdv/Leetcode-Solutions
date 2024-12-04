from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        values.sort()
        index = 0
        current = head
        while current:
            current.val = values[index]
            index += 1
            current = current.next
        return head
