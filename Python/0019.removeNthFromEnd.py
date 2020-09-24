"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # 1. Store Nodes
    # Time: O(n)
    # Space: O(n)
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head

        nodes = []
        cur = dummy
        while cur:
            nodes.append(cur)
            cur = cur.next

        parent = nodes[-n-1]
        parent.next = parent.next.next

        return dummy.next


    # 2. Two Passes, Find Length
    # Time: O(n)
    # Space: O(1)
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        cur = head

        while cur:
            cur = cur.next
            length += 1

        if n == length:
            return head.next

        cur = head
        for _ in range(length - n - 1): # Find parent
            cur = cur.next

        cur.next = cur.next.next

        return head

    # 3. One Pass, Two Pointers
    # Time: O(n)
    # Space: O(1)
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head

        fast = head
        prev = dummy

        for _ in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            prev = prev.next

        prev.next = prev.next.next

        return dummy.next
