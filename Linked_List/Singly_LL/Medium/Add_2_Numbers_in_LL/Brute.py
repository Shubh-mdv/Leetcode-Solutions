from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, ll: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur_node = ll
        count = 0
        while cur_node:
            # print(cur_node.val)
            front = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = front
            count += 1
        return prev, count

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        reversed_l1, lenL1 = self.reverse(l1)
        reversed_l2, lenL2 = self.reverse(l2)
        cur_node = reversed_l1
        numL1 = 0
        while lenL1 > 0 and cur_node:
            val = cur_node.val
            dig = val * (10 ** (lenL1 - 1))
            numL1 = numL1 + dig
            cur_node = cur_node.next
            lenL1 -= 1
        cur_node = reversed_l2
        numL2 = 0
        while lenL2 > 0 and cur_node:
            val = cur_node.val
            dig = val * (10 ** (lenL2 - 1))
            numL2 = numL2 + dig
            cur_node = cur_node.next
            lenL2 -= 1
        print("-----numL1-----", numL1)
        print("-----numL2-----", numL2)
        new_ll = numL1 + numL2
        print("------new_LL------", new_ll)
        temp = new_ll
        new_head = ListNode(0)
        current_node = new_head
        while temp > 0:
            print("----temp----", temp)
            dig = temp % 10
            print("----dig----", dig)
            new_node = ListNode(dig)
            current_node.next = new_node
            current_node = new_node
            temp = temp // 10
            print("----after temp----", temp)
        return self.reverse(new_head.next)


obj1 = ListNode(2)
obj2 = ListNode(4)
obj3 = ListNode(3)
obj1.next = obj2
obj2.next = obj3

obj4 = ListNode(5)
obj5 = ListNode(6)
obj6 = ListNode(4)
obj4.next = obj5
obj5.next = obj6

sol = Solution()
head = sol.addTwoNumbers(obj1, obj4)
cur_node = head
while cur_node:
    print(cur_node.val, "-->", end=" ")
    cur_node = cur_node.next
