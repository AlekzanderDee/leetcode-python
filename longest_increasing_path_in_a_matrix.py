"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

Difficulty:Hard

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]

Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]

Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""


class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        r_cnt = len(matrix)
        c_cnt = r_cnt and len(matrix[0])

        if not c_cnt:
            return 0

        dp = [[0] * c_cnt for _ in range(r_cnt)]

        def dfs(r_ind, c_ind):
            if not dp[r_ind][c_ind]:
                moves = [[-1, 0], [0, -1], [0, 1], [1, 0]]
                res = [1]
                for move in moves:
                    next_row = r_ind + move[0]
                    next_col = c_ind + move[1]
                    if 0 <= next_row < r_cnt and 0 <= next_col < c_cnt and \
                                    matrix[next_row][next_col] > matrix[r_ind][c_ind]:
                        res.append(1 + dfs(next_row, next_col))

                dp[r_ind][c_ind] = max(res)

            return dp[r_ind][c_ind]

        res = []
        for r_ind in range(r_cnt):
            for c_ind in range(c_cnt):
                res.append(dfs(r_ind, c_ind))

        return max(res)


if __name__ == "__main__":
    tests = [
        [
            [
                [9, 9, 4],
                [6, 6, 8],
                [2, 1, 1]
            ],
            4
        ],
        [
            [
                [3, 4, 5],
                [3, 2, 6],
                [2, 2, 1]
            ],
            4
        ],
        [
            [
                [15, 19, 1, 1, 19, 0, 3, 2, 4, 2, 6, 10, 16, 18, 8],
                [16, 11, 0, 13, 19, 12, 2, 14, 13, 6, 5, 14, 19, 5, 16],
                [18, 7, 8, 17, 7, 2, 8, 0, 12, 14, 18, 5, 16, 19, 0],
                [18, 9, 14, 5, 3, 7, 14, 0, 3, 16, 17, 10, 4, 4, 8],
                [11, 6, 2, 7, 0, 5, 1, 16, 7, 14, 9, 10, 6, 17, 2],
                [2, 5, 8, 8, 5, 10, 15, 14, 1, 6, 15, 12, 19, 10, 13],
                [7, 10, 5, 18, 4, 11, 1, 17, 14, 8, 6, 2, 10, 19, 6],
                [9, 16, 11, 15, 14, 7, 18, 0, 4, 6, 0, 15, 15, 14, 11],
                [12, 5, 9, 8, 2, 18, 9, 13, 14, 5, 18, 2, 13, 15, 14],
                [7, 4, 5, 7, 19, 0, 6, 15, 16, 16, 6, 7, 18, 2, 8],
                [6, 17, 10, 3, 10, 15, 10, 4, 17, 15, 11, 7, 9, 13, 13],
                [15, 6, 8, 14, 10, 18, 14, 13, 9, 19, 19, 15, 6, 17, 7],
                [15, 8, 7, 6, 14, 16, 16, 15, 2, 2, 7, 0, 0, 14, 8],
                [14, 2, 1, 10, 17, 6, 3, 1, 0, 1, 7, 1, 11, 15, 4],
                [17, 1, 16, 4, 11, 8, 14, 19, 13, 15, 9, 1, 17, 12, 13],
                [15, 18, 17, 11, 12, 14, 18, 14, 13, 16, 8, 17, 5, 15, 12],
                [18, 15, 18, 18, 18, 16, 4, 9, 0, 8, 16, 1, 5, 5, 9],
                [8, 2, 16, 7, 13, 0, 13, 13, 11, 4, 15, 8, 19, 12, 1],
                [6, 6, 2, 7, 17, 10, 16, 16, 19, 3, 10, 4, 9, 6, 11]
            ],
            10
        ],
        [
            [
                [7, 8, 9],
                [9, 7, 6],
                [7, 2, 3]
            ],
            6
        ],
        [
            [
                [16, 3, 15, 5, 9, 12, 15, 11, 16, 13, 0, 10, 13, 10, 19, 19, 8, 19, 5, 17, 0, 0, 1, 12, 7, 14, 6, 15,
                 18, 0, 0, 6, 17, 17, 18, 15, 16, 8, 6, 18, 8, 12, 2, 0, 1, 11, 8, 0, 1, 18, 5, 9, 6, 18, 18, 17, 6],
                [5, 7, 0, 4, 8, 13, 6, 6, 9, 0, 6, 14, 2, 10, 10, 14, 0, 15, 16, 9, 15, 10, 4, 8, 2, 13, 5, 5, 8, 18, 2,
                 7, 6, 14, 13, 7, 0, 6, 10, 0, 0, 12, 15, 11, 8, 7, 13, 9, 9, 8, 19, 5, 4, 15, 18, 1, 10],
                [10, 4, 13, 0, 17, 7, 0, 4, 6, 18, 1, 15, 19, 16, 14, 12, 11, 13, 15, 15, 10, 5, 1, 19, 13, 16, 13, 3,
                 6, 16, 5, 19, 8, 14, 6, 3, 3, 16, 17, 0, 8, 0, 0, 19, 13, 11, 16, 8, 12, 17, 10, 19, 1, 4, 3, 19, 13],
                [16, 5, 7, 19, 5, 3, 11, 14, 17, 0, 4, 13, 1, 1, 0, 0, 15, 9, 14, 18, 18, 3, 4, 5, 10, 16, 12, 10, 8,
                 10,12, 17, 6, 0, 2, 6, 0, 19, 4, 1, 18, 19, 9, 2, 18, 0, 3, 13, 6, 0, 8, 16, 15, 10, 8, 15, 5],
                [4, 13, 4, 15, 18, 10, 5, 19, 16, 14, 15, 15, 6, 1, 17, 3, 7, 12, 2, 19, 3, 18, 4, 14, 9, 3, 6, 9, 14,
                 13, 9, 5, 16, 3, 15, 12, 0, 14, 8, 7, 15, 12, 14, 1, 3, 19, 9, 4, 19, 10, 9, 4, 5, 7, 13, 2, 0],
                [9, 4, 12, 10, 6, 17, 15, 18, 10, 15, 14, 19, 7, 11, 17, 19, 0, 16, 14, 3, 8, 2, 12, 1, 7, 11, 18, 10,
                 0, 3, 7, 5, 7, 6, 3, 18, 4, 16, 3, 16, 6, 4, 11, 8, 17, 6, 1, 6, 1, 16, 1, 17, 3, 8, 12, 19, 15],
                [16, 15, 3, 8, 19, 0, 8, 17, 16, 8, 3, 14, 5, 16, 0, 2, 15, 2, 2, 16, 4, 12, 5, 5, 18, 16, 18, 8, 6, 3,
                 2, 5, 5, 8, 7, 16, 13, 2, 0, 3, 7, 18, 16, 15, 10, 6, 15, 16, 18, 14, 1, 13, 10, 10, 8, 6, 14],
                [18, 1, 0, 9, 18, 10, 6, 1, 9, 3, 3, 16, 8, 19, 9, 1, 5, 2, 6, 16, 11, 2, 6, 19, 1, 10, 19, 4, 18, 7, 0,
                 4, 7, 2, 6, 1, 16, 3, 18, 0, 3, 6, 13, 5, 11, 11, 18, 0, 13, 12, 12, 14, 4, 19, 16, 13, 6],
                [17, 14, 17, 4, 2, 1, 8, 3, 14, 10, 5, 6, 9, 1, 6, 0, 13, 18, 11, 14, 14, 3, 3, 14, 11, 11, 10, 15, 3,
                 12, 13, 11, 5, 18, 2, 14, 3, 14, 10, 1, 8, 19, 11, 19, 6, 14, 10, 9, 16, 0, 6, 13, 1, 2, 19, 16, 13, 18],
                [5, 12, 16, 9, 9, 19, 9, 1, 6, 10, 16, 12, 0, 18, 12, 16, 19, 4, 13, 18, 11, 9, 1, 9, 13, 1, 14, 16, 13,
                 2, 1, 0, 2, 17, 2, 1, 0, 0, 13, 17, 9, 7, 11, 18, 8, 1, 9, 9, 10, 7, 3, 7, 18, 8, 17, 17, 13],
                [1, 17, 8, 15, 7, 0, 18, 17, 19, 2, 5, 16, 2, 13, 13, 14, 10, 6, 10, 9, 2, 16, 16, 5, 17, 13, 7, 4, 3,
                 3, 7, 17, 16, 8, 12, 16, 1, 7, 19, 18, 6, 12, 9, 8, 10, 2, 2, 14, 2, 11, 18, 15, 9, 4, 4, 0, 10],
                [12, 0, 19, 8, 0, 15, 18, 10, 1, 14, 0, 10, 18, 16, 0, 5, 0, 12, 12, 18, 19, 3, 9, 8, 15, 19, 2, 2, 14,
                 2, 11, 16, 14, 15, 9, 4, 19, 9, 3, 0, 2, 7, 15, 4, 7, 19, 12, 17, 9, 15, 12, 3, 17, 12, 18, 12, 7],
                [1, 3, 5, 9, 1, 9, 2, 0, 11, 8, 11, 0, 10, 17, 18, 0, 11, 14, 10, 0, 10, 5, 17, 17, 11, 4, 17, 3, 13, 2,
                 17, 1, 4, 8, 14, 1, 17, 19, 6, 6, 18, 2, 18, 12, 1, 4, 11, 19, 9, 3, 7, 1, 16, 16, 1, 18, 17],
                [17, 1, 18, 19, 5, 3, 14, 7, 11, 17, 11, 2, 8, 12, 8, 2, 2, 19, 14, 10, 0, 4, 11, 19, 16, 17, 13, 14, 9,
                 19, 5, 16, 6, 9, 1, 12, 18, 19, 10, 15, 2, 6, 14, 16, 13, 13, 9, 8, 1, 11, 15, 2, 16, 0, 0, 11, 8],
                [11, 0, 6, 7, 8, 11, 18, 10, 6, 4, 19, 18, 4, 9, 0, 7, 18, 7, 4, 2, 9, 3, 12, 5, 15, 14, 8, 9, 0, 14, 6,
                 11, 4, 7, 3, 3, 7, 2, 17, 19, 1, 4, 1, 1, 12, 6, 6, 10, 15, 9, 1, 10, 7, 9, 1, 8, 5],
                [8, 4, 14, 7, 8, 11, 5, 18, 17, 2, 13, 14, 3, 7, 4, 4, 4, 12, 14, 0, 3, 17, 5, 18, 8, 4, 10, 11, 18, 1,
                 12, 10, 16, 6, 0, 10, 12, 12, 3, 16, 7, 16, 17, 9, 2, 8, 14, 1, 1, 3, 10, 10, 14, 8, 17, 0, 17],
                [12, 14, 11, 16, 10, 19, 11, 6, 19, 3, 5, 9, 19, 3, 2, 12, 14, 14, 1, 2, 2, 11, 14, 14, 18, 1, 14, 5,
                 16, 19, 3, 3, 9, 2, 16, 1, 1, 8, 10, 15, 2, 15, 6, 6, 13, 11, 12, 12, 7, 0, 13, 17, 19, 17, 13, 3, 18],
                [2, 15, 14, 13, 14, 4, 7, 11, 1, 4, 6, 18, 11, 17, 18, 3, 3, 4, 0, 6, 14, 6, 12, 0, 13, 18, 18, 8, 7,
                 12, 5, 2, 18, 6, 10, 11, 6, 8, 0, 11, 11, 7, 11, 4, 17, 6, 15, 6, 19, 9, 19, 13, 12, 12, 11, 8, 19],
                [16, 4, 17, 0, 17, 15, 6, 5, 18, 18, 17, 15, 17, 6, 19, 18, 16, 16, 16, 0, 7, 7, 0, 1, 9, 0, 4, 5, 10,
                 18, 14, 3, 2, 13, 10, 3, 6, 6, 14, 2, 4, 12, 9, 17, 13, 18, 17, 8, 12, 13, 18, 10, 3, 1, 16, 7, 17],
                [17, 17, 17, 12, 4, 5, 8, 8, 19, 2, 13, 13, 5, 3, 2, 19, 5, 9, 0, 6, 15, 17, 9, 10, 2, 6, 18, 5, 18, 11,
                 18, 13, 10, 1, 9, 10, 14, 6, 19, 15, 8, 15, 15, 13, 8, 4, 0, 0, 13, 17, 9, 14, 10, 2, 19, 15, 15],
                [12, 8, 7, 9, 11, 13, 4, 13, 11, 11, 8, 18, 11, 12, 15, 14, 7, 14, 13, 4, 13, 2, 14, 15, 3, 19, 11, 14,
                 12, 8, 3, 19, 7, 12, 16, 15, 18, 9, 19, 1, 1, 17, 10, 7, 11, 18, 3, 14, 2, 4, 11, 4, 3, 13, 6, 13, 9],
                [17, 11, 19, 7, 16, 9, 12, 13, 6, 15, 7, 11, 18, 13, 10, 1, 18, 4, 18, 15, 2, 4, 16, 14, 19, 2, 17, 13,
                 12, 0, 2, 9, 13, 1, 2, 15, 13, 13, 8, 16, 6, 6, 17, 19, 7, 7, 3, 0, 2, 6, 5, 13, 12, 9, 0, 1, 10],
                [10, 6, 3, 17, 15, 5, 4, 7, 8, 15, 9, 13, 12, 5, 8, 17, 16, 18, 1, 13, 12, 6, 2, 9, 0, 12, 7, 7, 3, 6,
                 13, 17, 14, 19, 5, 13, 3, 16, 17, 13, 18, 0, 16, 12, 1, 17, 3, 14, 13, 1, 13, 12, 13, 5, 11, 16, 10],
                [18, 12, 0, 9, 17, 12, 9, 8, 9, 4, 12, 1, 1, 11, 8, 14, 15, 5, 0, 9, 9, 7, 13, 9, 2, 15, 3, 17, 1, 6, 5,
                 5, 15, 5, 10, 12, 11, 6, 4, 11, 15, 11, 17, 13, 9, 1, 5, 12, 12, 2, 11, 8, 17, 9, 14, 8, 2],
                [4, 7, 5, 11, 0, 14, 3, 12, 17, 19, 7, 2, 5, 4, 3, 18, 2, 4, 14, 0, 4, 7, 3, 18, 5, 5, 17, 5, 9, 1, 10,
                 9, 14, 0, 8, 5, 13, 18, 1, 16, 0, 13, 15, 12, 7, 12, 12, 5, 10, 15, 4, 18, 16, 2, 5, 17, 5],
                [15, 5, 13, 3, 18, 15, 6, 0, 1, 7, 0, 1, 1, 4, 11, 10, 4, 7, 19, 13, 3, 6, 17, 1, 0, 0, 7, 8, 2, 17, 14,
                 3, 1, 7, 13, 2, 14, 11, 5, 7, 11, 9, 3, 11, 15, 2, 14, 0, 5, 16, 0, 15, 16, 9, 9, 17, 8],
                [14, 19, 6, 11, 7, 0, 6, 15, 4, 5, 11, 7, 2, 10, 9, 9, 3, 4, 1, 0, 12, 5, 1, 8, 2, 12, 16, 8, 9, 5, 6,
                 18, 5, 10, 12, 17, 15, 11, 10, 4, 7, 16, 6, 7, 12, 14, 9, 13, 5, 14, 1, 9, 15, 6, 9, 17, 0],
                [1, 18, 4, 2, 18, 18, 15, 14, 19, 19, 13, 13, 12, 19, 17, 17, 16, 19, 9, 9, 9, 11, 9, 2, 9, 16, 13, 13,
                 4, 1, 15, 10, 16, 11, 13, 4, 15, 7, 11, 16, 4, 11, 18, 13, 7, 14, 9, 1, 11, 2, 9, 5, 18, 12, 17, 2, 0],
                [17, 19, 4, 4, 15, 19, 1, 12, 8, 1, 19, 4, 17, 5, 4, 7, 7, 12, 15, 6, 18, 14, 0, 14, 2, 16, 0, 17, 15,
                 18, 18, 17, 6, 13, 18, 8, 9, 0, 5, 15, 17, 10, 12, 14, 2, 2, 1, 2, 5, 15, 19, 3, 7, 9, 1, 6, 8],
                [12, 2, 14, 4, 8, 6, 18, 17, 18, 17, 7, 3, 12, 17, 8, 9, 3, 13, 0, 4, 18, 0, 3, 3, 7, 5, 2, 1, 17, 5,
                 17, 0, 11, 19, 19, 7, 7, 5, 8, 7, 11, 8, 10, 15, 12, 1, 11, 10, 5, 3, 3, 2, 17, 5, 19, 10, 8],
                [17, 2, 17, 16, 19, 8, 14, 19, 12, 17, 1, 18, 16, 15, 0, 18, 2, 8, 19, 3, 15, 11, 18, 10, 6, 14, 16, 2,
                 11, 14, 13, 15, 19, 15, 6, 19, 16, 15, 1, 18, 7, 2, 17, 6, 10, 19, 19, 5, 1, 14, 14, 3, 8, 1, 14, 7, 7],
                [14, 19, 5, 10, 0, 18, 2, 15, 2, 16, 13, 8, 18, 3, 7, 17, 17, 19, 2, 16, 12, 5, 18, 0, 7, 17, 17, 7, 14,
                 17, 13, 0, 14, 18, 0, 3, 5, 15, 15, 2, 14, 8, 0, 18, 12, 6, 15, 15, 15, 12, 7, 1, 14, 7, 11, 14, 19],
                [3, 4, 13, 16, 1, 7, 6, 10, 17, 9, 18, 5, 17, 17, 2, 8, 13, 5, 10, 19, 10, 16, 11, 11, 14, 5, 10, 17,
                 10, 11, 13, 19, 16, 5, 9, 8, 0, 1, 10, 11, 12, 0, 14, 8, 12, 12, 4, 15, 11, 11, 1, 2, 1, 8, 2, 5, 7],
                [8, 14, 1, 5, 3, 12, 2, 16, 0, 0, 10, 7, 15, 14, 12, 0, 3, 19, 18, 19, 13, 17, 7, 6, 4, 7, 4, 13, 1, 17,
                 2, 15, 19, 10, 5, 15, 13, 15, 13, 11, 9, 17, 14, 14, 1, 7, 6, 16, 11, 2, 18, 4, 10, 19, 13, 19, 5],
                [19, 10, 0, 17, 6, 17, 1, 19, 13, 15, 7, 14, 6, 19, 2, 7, 2, 0, 12, 16, 10, 4, 12, 3, 11, 2, 9, 9, 3, 0,
                 13, 5, 10, 17, 4, 19, 15, 11, 0, 19, 8, 9, 10, 15, 12, 8, 4, 6, 15, 8, 6, 10, 9, 18, 13, 5, 5],
                [8, 3, 4, 6, 1, 12, 17, 19, 19, 1, 15, 2, 15, 19, 8, 11, 8, 12, 19, 15, 13, 6, 12, 17, 1, 13, 13, 2, 5,
                 14, 18, 9, 17, 17, 5, 6, 15, 1, 5, 2, 1, 1, 2, 9, 2, 3, 2, 8, 9, 4, 6, 10, 5, 3, 3, 3, 9],
                [2, 0, 4, 16, 3, 18, 10, 17, 1, 15, 0, 6, 11, 16, 17, 15, 10, 10, 3, 3, 14, 0, 6, 10, 3, 12, 5, 1, 3, 3,
                 19, 14, 8, 3, 18, 0, 12, 16, 5, 0, 17, 19, 5, 3, 10, 15, 1, 1, 17, 13, 15, 10, 11, 19, 19, 16, 2],
                [17, 4, 8, 10, 14, 10, 18, 18, 6, 18, 12, 18, 17, 5, 14, 10, 11, 3, 1, 2, 6, 1, 15, 14, 10, 19, 0, 10,
                 19, 12, 11, 19, 2, 3, 14, 12, 18, 6, 19, 3, 18, 19, 16, 4, 9, 15, 11, 12, 9, 4, 13, 4, 0, 7, 5, 1, 17],
                [5, 12, 8, 8, 12, 18, 14, 1, 10, 0, 18, 3, 3, 10, 8, 1, 12, 13, 14, 15, 18, 19, 18, 19, 7, 2, 15, 6, 11,
                 18, 17, 10, 3, 10, 4, 5, 11, 19, 13, 16, 1, 10, 19, 19, 16, 19, 1, 13, 3, 10, 1, 8, 3, 14, 18, 7, 19],
                [1, 7, 12, 6, 16, 3, 9, 12, 11, 6, 18, 6, 5, 6, 10, 13, 2, 12, 16, 2, 14, 17, 1, 7, 4, 4, 7, 6, 19, 2,
                 8, 18, 1, 13, 9, 19, 17, 7, 2, 8, 15, 3, 1, 13, 11, 18, 3, 12, 14, 11, 10, 8, 7, 6, 9, 15, 18],
                [3, 13, 2, 0, 15, 18, 11, 6, 8, 18, 15, 15, 5, 2, 7, 12, 13, 0, 3, 19, 13, 4, 11, 2, 2, 11, 2, 18, 14,
                 13, 17, 12, 14, 2, 19, 15, 13, 18, 13, 4, 12, 19, 14, 4, 0, 0, 4, 0, 10, 15, 9, 19, 6, 7, 10, 1, 1],
                [9, 6, 11, 14, 9, 12, 11, 14, 6, 2, 2, 3, 14, 6, 1, 13, 19, 11, 13, 6, 8, 5, 7, 6, 16, 14, 4, 11, 5, 5,
                 7, 14, 8, 18, 9, 17, 6, 16, 6, 2, 8, 3, 7, 10, 0, 1, 18, 0, 3, 14, 2, 13, 10, 1, 12, 3, 1],
                [11, 3, 14, 19, 1, 1, 19, 6, 6, 10, 17, 18, 1, 14, 18, 1, 5, 3, 2, 18, 14, 5, 12, 19, 4, 11, 6, 14, 12,
                 3, 7, 10, 0, 14, 16, 16, 12, 18, 15, 0, 11, 8, 8, 7, 11, 18, 7, 8, 4, 2, 7, 18, 8, 1, 9, 10, 9],
                [0, 0, 16, 18, 13, 17, 0, 7, 14, 17, 0, 7, 14, 6, 17, 4, 1, 7, 16, 14, 15, 4, 14, 5, 12, 9, 4, 1, 7, 15,
                 17, 4, 13, 5, 5, 15, 17, 14, 11, 11, 7, 0, 11, 19, 6, 9, 19, 18, 19, 2, 1, 18, 4, 9, 15, 4, 1],
                [3, 6, 16, 10, 7, 3, 6, 13, 15, 19, 15, 12, 9, 19, 14, 4, 14, 10, 14, 9, 19, 7, 4, 11, 1, 10, 11, 17,
                 18, 18, 16, 16, 6, 9, 9, 15, 0, 5, 2, 10, 11, 0, 6, 9, 2, 11, 4, 19, 8, 11, 14, 0, 8, 1, 3, 9, 3],
                [4, 13, 19, 12, 12, 10, 3, 14, 6, 8, 5, 3, 3, 5, 15, 17, 19, 16, 16, 5, 4, 14, 11, 15, 16, 9, 14, 5, 0,
                 3, 17, 9, 9, 16, 17, 2, 9, 13, 13, 11, 15, 9, 0, 2, 13, 14, 11, 16, 16, 1, 6, 6, 10, 8, 11, 18, 12],
                [5, 8, 16, 5, 11, 19, 19, 11, 8, 11, 8, 1, 6, 1, 1, 10, 12, 9, 15, 6, 10, 3, 14, 4, 18, 6, 10, 16, 13,
                 1, 19, 10, 4, 5, 11, 3, 16, 19, 9, 9, 1, 14, 14, 15, 8, 1, 11, 6, 9, 3, 9, 15, 4, 0, 9, 1, 17],
                [1, 12, 15, 13, 3, 4, 1, 12, 17, 10, 3, 1, 12, 2, 3, 8, 9, 17, 19, 16, 11, 6, 12, 16, 14, 13, 11, 17, 8,
                 14, 9, 7, 10, 13, 14, 2, 2, 15, 2, 3, 13, 3, 1, 14, 16, 12, 5, 11, 5, 16, 3, 2, 16, 10, 14, 9, 11],
                [10, 19, 9, 0, 17, 18, 0, 17, 0, 11, 13, 6, 8, 6, 11, 16, 0, 1, 8, 1, 9, 7, 7, 17, 11, 13, 5, 16, 7, 13,
                 16, 6, 16, 19, 2, 12, 13, 14, 8, 15, 1, 15, 8, 11, 9, 14, 11, 3, 12, 10, 7, 13, 6, 10, 0, 18, 3],
                [13, 13, 19, 8, 2, 18, 13, 11, 7, 3, 8, 19, 4, 0, 12, 16, 5, 11, 9, 8, 17, 6, 17, 8, 9, 18, 10, 10, 13,
                 11, 7, 19, 1, 19, 9, 10, 16, 17, 11, 3, 18, 14, 11, 19, 5, 2, 10, 17, 7, 5, 16, 6, 7, 6, 6, 7, 1],
                [2, 13, 15, 11, 2, 0, 15, 3, 15, 18, 9, 11, 10, 17, 13, 17, 7, 19, 1, 19, 3, 3, 17, 10, 19, 0, 7, 8, 14,
                 7, 5, 7, 6, 15, 11, 18, 15, 6, 8, 3, 8, 10, 5, 7, 5, 13, 5, 11, 8, 11, 13, 8, 8, 19, 11, 1, 1],
                [13, 11, 0, 2, 11, 2, 15, 15, 10, 11, 1, 4, 12, 8, 3, 6, 4, 14, 8, 3, 7, 13, 9, 14, 2, 6, 14, 15, 9, 4,
                 18, 1, 18, 17, 19, 9, 11, 2, 12, 17, 2, 7, 5, 2, 3, 9, 13, 10, 2, 19, 7, 14, 1, 15, 3, 11, 9],
                [13, 11, 6, 9, 10, 2, 14, 9, 19, 18, 5, 14, 18, 19, 2, 9, 18, 16, 6, 10, 7, 9, 0, 2, 17, 14, 15, 14, 18,
                 16, 3, 1, 6, 2, 15, 4, 11, 12, 2, 8, 3, 7, 13, 0, 9, 8, 5, 2, 10, 12, 14, 5, 4, 0, 11, 10, 16],
                [15, 3, 15, 2, 1, 9, 8, 17, 19, 8, 9, 14, 2, 9, 1, 9, 0, 13, 6, 4, 11, 16, 5, 13, 12, 0, 13, 6, 6, 16,
                 0,  16, 5, 8, 14, 12, 18, 10, 15, 13, 15, 3, 4, 4, 17, 0, 2, 19, 16, 9, 7, 18, 7, 19, 17, 16, 11],
                [3, 5, 4, 19, 14, 13, 16, 8, 0, 3, 18, 2, 9, 6, 8, 0, 18, 14, 8, 0, 7, 4, 3, 15, 9, 0, 3, 12, 19, 16,
                 18, 7, 10, 2, 19, 2, 10, 1, 5, 8, 5, 13, 18, 15, 15, 13, 8, 16, 12, 10, 6, 16, 5, 7, 7, 18, 17]
            ],
            11
        ]
    ]

    s = Solution()
    for test in tests:
        res = s.longestIncreasingPath(test[0])
        if test[1] != res:
            print("Input {} Got {} Wanted {}".format(test[0], res, test[1]))

    print("Completed")