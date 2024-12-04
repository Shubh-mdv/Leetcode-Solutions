from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        lenA = 0
        lenB = 0
        current1 = headA
        while current1:
            lenA += 1
            current1 = current1.next
        current2 = headB
        while current2:
            lenB += 1
            current2 = current2.next
        diff = abs(lenA - lenB)
        if lenA > lenB:
            current1 = headA
            temp_diff = diff
            while current1:
                if temp_diff > 0:
                    current1 = current1.next
                    temp_diff -= 1
                else:
                    break
            current2 = headB
            temp_lenB = lenB
            while temp_lenB > 0:
                if current1 is current2:
                    return current1
                else:
                    current1 = current1.next
                    current2 = current2.next
                    temp_lenB -= 1
            return None
        elif lenB > lenA:
            current2 = headB
            temp_diff = diff
            while current2:
                if temp_diff > 0:
                    current2 = current2.next
                    temp_diff -= 1
                else:
                    break
            current1 = headA
            temp_lenA = lenA
            while temp_lenA > 0:
                if current2 is current1:
                    return current1
                else:
                    current2 = current2.next
                    current1 = current1.next
                    temp_lenA -= 1
            return None
        else:
            current1 = headA
            current2 = headB
            while lenA > 0:
                if current1 is current2:
                    return current1
                else:
                    current2 = current2.next
                    current1 = current1.next
                    lenA -= 1
            return None
