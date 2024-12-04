from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        count = 0
        current = head
        while current.next:
            count += 1
            current = current.next
        mid = 0
        current = head
        while mid < count // 2:
            current = current.next
            mid += 1
        return current
