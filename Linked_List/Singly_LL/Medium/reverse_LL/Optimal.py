from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        current = head
        prev = None
        while current:
            front = current.next
            current.next = prev
            prev = current
            current = front

        return prev
