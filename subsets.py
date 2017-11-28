"""
https://leetcode.com/problems/subsets/description/

Difficulty:Medium

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""


class Solution:
    def get_subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []

        res = [[nums[0]]]

        sub_subsets = self.get_subsets(nums[1:])
        for s_set in sub_subsets:
            res.append([nums[0]] + s_set)
            res.append(s_set)
        return res

    def subsets(self, nums):
        return [[]] + self.get_subsets(nums)


if __name__ == "__main__":
    tests = [
        [
            [1, 2, 3],
            [[], [1], [1, 2], [2], [1, 2, 3], [2, 3], [1, 3], [3]]
        ],
        [
            [],
            [[]],
        ],
        [
            [1],
            [[], [1]],
        ],
        [
            [1, 2],
            [[], [1], [1, 2], [2]]
        ]

    ]

    s = Solution()

    for test in tests:
        res = s.subsets(test[0])
        if res != test[1]:
            print("Error. input \"{}\" wanted {} got {}".format(test[0], test[1], res))

    print("completed")
