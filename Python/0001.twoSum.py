"""
https://leetcode.com/problems/two-sum/

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution:

    # 1. Hash Table with Two Loops
    # Time: O(n)
    # Space: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {} # {num: idx}

        for idx, num in enumerate(nums):
            hash_table[num] = idx

        for idx, num in enumerate(nums):
            other = target - num
            if other in hash_table and idx != hash_table[other]:
                return [idx, hash_table[other]]

        return [None, None]


    # 2. Hash Table with One Loop
    # Time: O(n)
    # Space: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {} # {num: idx}

        for idx, num in enumerate(nums):
            other = target - num
            if other in hash_table:
                return [idx, hash_table[other]]

            hash_table[num] = idx

        return [None, None]


    # * N Sums Pattern
    # https://github.com/gigglegrig/LeetCode/wiki/*-N-Sum
