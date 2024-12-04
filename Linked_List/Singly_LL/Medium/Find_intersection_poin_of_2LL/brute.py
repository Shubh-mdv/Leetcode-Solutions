from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        current = headA
        all_nodes = set()
        while current:
            all_nodes.add(current)
            current = current.next

        current = headB
        while current:
            if current in all_nodes:
                return current
            else:
                current = current.next
        return None
