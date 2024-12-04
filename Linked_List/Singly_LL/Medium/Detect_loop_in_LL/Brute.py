from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        current = head
        node_set = set()
        while current:
            if current not in node_set:
                node_set.add(current)
                current = current.next
            else:
                return True
        return False
