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
        stack = []
        while current:
            ele = current.val
            stack.append(ele)
            current = current.next
        current = head
        while current:
            ele_poped = stack.pop()
            current.val = ele_poped
            current = current.next

        return head
