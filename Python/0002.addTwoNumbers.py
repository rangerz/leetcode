"""
https://leetcode.com/problems/add-two-numbers/

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # 1. Straight
    # Time: O(n)
    # Space: O(1)
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = dummy = ListNode()
        carry = 0

        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            head.next = ListNode(carry % 10)
            carry //= 10
            head = head.next

        if 1 == carry:
            head.next = ListNode(1)

        return dummy.next


    # 2. Recursive
    # Time: O(n)
    # Space: O(1)
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1

        target = l1.val + l2.val
        res = ListNode(target % 10)
        res.next = self.addTwoNumbers(l1.next, l2.next)

        if 1 == target // 10:
            res.next = self.addTwoNumbers(res.next, ListNode(1))

        return res
