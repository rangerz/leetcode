"""
https://leetcode.com/problems/intersection-of-two-linked-lists/

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # 1. Find the length
    # Time: O(n)
    # Space: O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        def getLength(node):
            length = 0
            while node:
                node = node.next
                length += 1
            return length

        lenA = getLength(headA)
        lenB = getLength(headB)

        if lenA < lenB:
            lenA, lenB = lenB, lenA
            headA, headB = headB, headA

        for _ in range(lenA - lenB):
            headA = headA.next

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA


    # 2. To tail and switch to other's head
    # Time: O(n)
    # Space: O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p = headA
        q = headB

        if not p or not q:
            return None

        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA

        return p