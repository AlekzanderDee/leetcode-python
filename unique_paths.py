"""
https://leetcode.com/problems/unique-paths/description/

Difficulty:Medium

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
"""


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0

        pre = [1] * n
        cur = [1] * n

        for i in range(1, m):
            for k in range(1, n):
                cur[k] = pre[k] + cur[k-1]

            cur, pre = pre, cur

        return pre[-1]


if __name__ == "__main__":
    tests = [
        [3, 3, 6],
        [3, 7, 28],
        [3, 10, 55],
        [1, 10, 1],
        [0, 0, 0],
    ]
    s = Solution()
    for test in tests:
        res = s.uniquePaths(test[0], test[1])
        if test[2] != res:
            print("Inputs {}, {} Got {} Wanted {}".format(test[0], test[1], res, test[2]))

    print("Completed")