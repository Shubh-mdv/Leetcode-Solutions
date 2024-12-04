from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        if length == n:
            new_head = head.next
            head.next = None
            return new_head
        steps = length - n
        current = head
        while current:
            steps -= 1
            if steps == 0:
                break
            current = current.next
        current.next = current.next.next
        return head
