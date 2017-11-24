"""
Difficulty:Medium

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.
Note: n will be less than 15,000.

Example 1:

Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.

Example 2:

Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:

Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""


class Solution:

    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_len = len(nums)
        if nums_len < 3:
            return False

        min_left = nums[0]
        for j in range(1, nums_len - 1):

            for k in range(j + 1, nums_len):
                if nums[j] > nums[k] > min_left:
                    return True

            min_left = min((min_left, nums[j]))

        return False


if __name__ == '__main__':
    tests = [
        [[1, 2, 3, 4], False],
        [[-1, 3, 2, 0], True],
        [[3, 1, 4, 2], True],
        [[8,10,4,6,5], True],
        [[2,4,3,1], True],
    ]

    s = Solution()
    for test in tests:
        res = s.find132pattern(test[0])
        if test[1] != res:
            print("Test nums {} Got {} Wanted {}".format(test[0], res, test[1]))

    print("Completed")
