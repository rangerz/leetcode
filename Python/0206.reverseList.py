"""
https://leetcode.com/problems/reverse-linked-list/

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow Up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # 1. Iter
    # Time: O(n)
    # Space: O(1)
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        while head:
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp

        return new_head

    # 2. Recursive
    # Time: O(n)
    # Space: O(1)
    def reverseList(self, head: ListNode) -> ListNode:
        def doReverse(head, new_head):
            if head == None:
                return new_head
            nxt = head.next
            head.next = new_head
            return doReverse(nxt, head)

        return doReverse(head, None)
