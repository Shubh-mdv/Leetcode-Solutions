from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        print(fast)
        if not fast:
            new_head = head.next
            head.next = None
            return new_head
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
