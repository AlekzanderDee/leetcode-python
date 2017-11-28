"""
https://leetcode.com/problems/set-matrix-zeroes/description/

Difficulty:Medium

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.
Follow up:

Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

"""


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        row_cnt = len(matrix)
        col_cnt = len(matrix[0])

        if any((row_cnt == 0, col_cnt == 0)):
            return

        for r_ind in range(row_cnt):
            if matrix[r_ind][0] == 0:
                col0 = 0

            for c_ind in range(1, col_cnt):
                if matrix[r_ind][c_ind] == 0:
                    matrix[r_ind][0] = matrix[0][c_ind] = 0

        for r_ind in range(row_cnt - 1, -1, -1):
            for c_ind in range(col_cnt - 1, 0, -1):
                if matrix[r_ind][0] == 0 or matrix[0][c_ind] == 0:
                    matrix[r_ind][c_ind] = 0
            if col0 == 0:
                matrix[r_ind][0] = 0


if __name__ == "__main__":
    tests = [
        [
            [[0]],
            [[0]],
        ],
        [
            [[]],
            [[]],
        ],
        [
            [[1, 0, 3],
             [3, 4, 5]],
            [[0, 0, 0],
             [3, 0, 5]],
        ],
        [
            [[1, 1, 1],
             [0, 1, 2]],
            [[0, 1, 1],
             [0, 0, 0]],
        ],

    ]
    s = Solution()
    for test in tests:
        s.setZeroes(test[0])
        if test[0] != test[1]:
            print("Error. wanted {} got {}".format(test[1], test[0]))

    print("completed")
