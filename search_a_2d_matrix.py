"""
https://leetcode.com/problems/search-a-2d-matrix/description/

Difficulty:Medium

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

Given target = 3, return true
"""


class Solution:
    def bs(self, array, target):
        if not len(array):
            return False

        mid = len(array) // 2

        if target == array[mid]:
            return True
        elif target > array[mid]:
            return self.bs(array[mid+1:], target)
        else:
            return self.bs(array[:mid], target)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row_cnt = len(matrix)
        col_cnt = row_cnt and len(matrix[0])
        if not col_cnt:
            return False

        row_pointer = 0
        col_pointer = col_cnt - 1

        while True:
            if target == matrix[row_pointer][col_pointer]:
                return True
            elif target > matrix[row_pointer][col_pointer]:
                if row_pointer < row_cnt - 1:
                    row_pointer += 1
                else:
                    return False
            else:
                return self.bs(matrix[row_pointer], target)



if __name__ == "__main__":
    tests = [
        [
            [
                [1, 3, 5, 7],
                [10, 11, 16, 20],
                [23, 30, 34, 50]
            ],
            3,
            True
        ],
        [
            [
                [1, 3, 5, 7],
                [10, 11, 16, 20],
                [23, 30, 34, 50]
            ],
            7,
            True
        ],
        [
            [
                [1, 3, 5, 7],
                [10, 11, 16, 20],
                [23, 30, 34, 50]
            ],
            11,
            True
        ],
        [
            [
                [1, 3, 5, 7],
                [10, 11, 16, 20],
                [23, 30, 34, 50]
            ],
            31,
            False
        ],
        [
            [
                [1, 3, 5, 7],
                [10, 11, 16, 20],
                [23, 30, 34, 50]
            ],
            63,
            False
        ],
        [
            [
                [1, 3, 5, 7],
                [10, 11, 16, 20],
                [23, 30, 34, 50]
            ],
            -3,
            False
        ],
    ]

    s = Solution()
    for test in tests:
        res = s.searchMatrix(test[0], test[1])
        if test[2] != res:
            print("Input {} Got {} Wanted {}".format(test[1], res, test[2]))

    print("Completed")
