"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0
"""

class Solution:

    # 1. Sliding Window + Dict
    # Time: O(n)
    # Space: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        chars = {} # {char: idx}
        left = 0

        for right, char in enumerate(s):
            if char in chars:
                left = max(left, chars[char] + 1)
            chars[char] = right
            res = max(res, right - left + 1)

        return res


    # 2. Sliding Window + Set
    # Time: O(n)
    # Space: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        chars = set() # {char}
        left, right = 0, 0

        while left < len(s) and right < len(s):
            if s[right] in chars:
                chars.remove(s[left])
                left += 1
            else:
                chars.add(s[right])
                right += 1
                res = max(res, len(chars))

        return res



