"""
https://leetcode.com/problems/longest-consecutive-sequence/description/

Difficulty:Hard

 Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

import heapq

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_len, cur_len = 1, 1
        heapq.heapify(nums)
        num = heapq.heappop(nums)

        while nums:
            next_num = heapq.heappop(nums)
            if next_num == num + 1:
                cur_len += 1
                num = next_num

            elif next_num > num + 1:
                if cur_len > max_len:
                    max_len = cur_len
                cur_len = 1
                num = next_num

        if cur_len > max_len:
            max_len = cur_len

        return max_len


if __name__ == "__main__":
    tests = [
        [
            [100, 4, 200, 1, 3, 2],
            4
        ],
        [
            [],
            0
        ],
        [
            [100, 4, 200, 1, 4, 3, 2, 1],
            4
        ],
        [
            [100, 2, 43, 4],
            1
        ]
    ]

    s = Solution()
    for test in tests:
        res = s.longestConsecutive(test[0])
        if test[1] != res:
            print("Input {} Got {} Wanted {}".format(test[0], res, test[1]))

    print("Completed")

