"""
Difficulty:Medium

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note: All inputs will be in lower-case.
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_groups = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_groups[sorted_word].append(word)

        return list(anagram_groups.values())


if __name__ == "__main__":
    tests = [
        [
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [
                ["ate", "eat", "tea"],
                ["nat", "tan"],
                ["bat"]
            ]
        ]
    ]

    s = Solution()
    for test in tests:
        res = s.groupAnagrams(test[0])
        if res.sort() != test[1].sort():
            print("Error. input \"{}\" wanted {} got {}".format(test[0], test[1], res))

    print("completed")