"""
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/

Difficulty:Medium

 Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

"""

from collections import Counter


class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return len(s)

        if len(s) < k:
            return 0

        c = Counter(s)
        min_cnt = 0
        sep = None
        for ch, ch_cnt in c.most_common()[::-1]:
            if ch_cnt < k and ch_cnt > min_cnt:
                min_cnt = ch_cnt
                sep = ch
            elif ch_cnt >= k:
                break

        if not sep:
            return len(s)

        parts = s.split(sep)

        return max([self.longestSubstring(part, k) for part in parts])


if __name__ == "__main__":
    s = Solution()
    s.longestSubstring("aaabb", 3) == 3
    s.longestSubstring("ababbc", 2) == 5

    print("Completed")
