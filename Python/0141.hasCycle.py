"""
https://leetcode.com/problems/linked-list-cycle/

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 1. Set
    # Time: O(n)
    # Space: O(n)
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()

        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next

        return False

    # 2. Two Pointers
    # Time: O(n)
    # Space: O(1)
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False
