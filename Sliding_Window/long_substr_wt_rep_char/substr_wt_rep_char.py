"""Given a string s, find the length of the longest
substring
without repeating characters.



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
"""

def lengthOfLongestSubstring(s):
    charS = set()
    l = 0
    res = 0
    for c in range(len(s)):
        while s[c] in charS:
            charS.remove(s[l])
            l += 1
        charS.add(s[c])
        res = max(res, c - l + 1)
    return res

if __name__ == "__main__":
    s = input()
    print(lengthOfLongestSubstring(s))
