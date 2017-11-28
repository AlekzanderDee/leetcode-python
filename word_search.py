"""
https://leetcode.com/problems/word-search/description/

Difficulty:Medium

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""


class Solution:
    def search_path(self, board, word, i, j):

        word_len = len(word)
        if word_len == 0:
            return True

        row_cnt = len(board)
        col_cnt = len(board[0])

        if i < 0 or i == row_cnt or j < 0 or j == col_cnt or board[i][j] != word[0]:
            return False

        saved_val = board[i][j]
        board[i][j] = "-"
        res = self.search_path(board, word[1:], i - 1, j) or \
              self.search_path(board, word[1:], i + 1, j) or \
              self.search_path(board, word[1:], i, j - 1) or \
              self.search_path(board, word[1:], i, j + 1)

        board[i][j] = saved_val
        return res

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        word_len = len(word)
        if word_len == 0:
            return True

        row_cnt = len(board)
        if row_cnt == 0:
            return False

        col_cnt = len(board[0])

        for i in range(row_cnt):
            for j in range(col_cnt):
                if self.search_path(board, word, i, j):
                    return True

        return False


if __name__ == "__main__":
    tests = [
        [
            [
                ['A', 'B', 'C', 'E'],
                ['S', 'F', 'C', 'S'],
                ['A', 'D', 'E', 'E']
            ],
            "ABCCED",
            True,
        ],
        [
            [
                ['A', 'B', 'C', 'E'],
                ['S', 'F', 'C', 'S'],
                ['A', 'D', 'E', 'E']
            ],
            "SEE",
            True,
        ],
        [
            [
                ['A', 'B', 'C', 'E'],
                ['S', 'F', 'C', 'S'],
                ['A', 'D', 'E', 'E']
            ],
            "ABCB",
            False,
        ]
    ]

    s = Solution()

    for test in tests:
        res = s.exist(test[0], test[1])
        if res != test[2]:
            print("Error. word \"{}\" wanted {} got {}".format(test[1], test[2], res))

    print("completed")
