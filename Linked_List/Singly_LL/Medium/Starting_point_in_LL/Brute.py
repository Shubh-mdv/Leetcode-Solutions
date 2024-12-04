from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        my_set = set()
        current = head
        while current:
            if current not in my_set:
                my_set.add(current)
                current = current.next
            else:
                return current
        return None
