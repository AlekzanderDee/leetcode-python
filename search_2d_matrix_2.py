"""
https://leetcode.com/problems/search-a-2d-matrix-ii/description/

Difficulty:Medium

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.

Given target = 20, return false.
"""


class Solution_1:
    def b_search(self, row, target):
        if not row:
            return False
        mid = len(row) // 2
        return row[mid] == target or self.b_search(row[:mid], target) or self.b_search(row[mid+1:], target)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        for row in matrix:
            if row[0] <= target <= row[-1] and self.b_search(row, target):
                return True

        return False

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row_cnt = len(matrix)
        if row_cnt == 0 or len(matrix[0]) == 0:
            return False
        col_cnt = len(matrix[0])

        # top right corner of the matrix
        row_ind = 0
        col_ind = col_cnt - 1

        while row_ind < row_cnt and col_ind >= 0:
            val = matrix[row_ind][col_ind]
            if val == target:
                return True

            if val < target:
                row_ind += 1
            else:
                col_ind -= 1

        return False


if __name__ == "__main__":
    tests = [
        [
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]
            ],
            5,
            True
        ],
        [
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]
            ],
            20,
            False
        ],
        [
            [[-5]],
            - 10,
            False
        ]

    ]

    s = Solution()
    for test in tests:
        res = s.searchMatrix(test[0], test[1])
        if test[2] != res:
            print("Searched for {} Got {} Wanted {}".format(test[1], res, test[2]))

    print("Completed")




