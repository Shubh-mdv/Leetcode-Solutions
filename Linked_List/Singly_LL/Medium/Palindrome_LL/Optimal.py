from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            front = current.next
            current.next = prev
            prev = current
            current = front
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        new_head = self.reverse_list(slow.next)
        first = head
        second = new_head
        while second:
            if second.val != first.val:
                return False
            first = first.next
            second = second.next
        self.reverse_list(new_head)
        return True
