"""
https://leetcode.com/problems/number-of-islands/description/

Difficulty:Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000

Answer: 1

Example 2:

11000
11000
00100
00011

Answer: 3
"""
class Solution:
    def growIsland(self, r, c, grid):
        grid[r][c] = '*'
        neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for dr, dc in neighbors:
            if 0 <= (r + dr) < len(grid) and 0 <= (c + dc) < len(grid[0]) and grid[r+dr][c+dc] == "1":
                self.growIsland(r + dr, c + dc, grid)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row_cnt = len(grid)
        if row_cnt == 0:
            return 0

        col_cnt = len(grid[0])
        if col_cnt == 0:
            return 0

        islands_count = 0

        for r in range(row_cnt):
            for c in range(col_cnt):

                if grid[r][c] == "1":
                    self.growIsland(r, c, grid)
                    islands_count += 1

        return islands_count


if __name__ == "__main__":
    tests = [
        [
            [
                "1 1 0 0 0".split(),
                "1 1 0 0 0".split(),
                "0 0 1 0 0".split(),
                "0 0 0 1 1".split()
            ],
            3
        ],
        [
            [
                "1 1 0 0 1".split(),
                "1 1 0 0 0".split(),
                "0 0 0 0 1".split(),
                "0 1 0 1 1".split()
            ],
            4
        ],
        [
            [
                "1 1 0 0 0".split(),
                "1 1 0 0 0".split(),
                "0 0 0 0 0".split(),
                "0 0 0 0 0".split()
            ],
            1
        ],
        [
            [
                "1 1 1 1 0".split(),
                "1 1 0 1 0".split(),
                "1 1 0 0 0".split(),
                "0 0 0 0 0".split()
            ],
            1
        ],
        [
            [
                "1 1 1 1 0".split(),
                "1 1 0 1 0".split(),
                "1 1 0 0 0".split(),
                "0 0 0 0 0".split()
            ],
            1
        ],
        [
            [
                "0 0".split(),
                "0 0".split(),
                "0 0".split(),
            ],
            0
        ],
        [
            [
                "1 0".split(),
                "0 1".split(),
                "1 0".split(),
            ],
            3
        ],
        [
            [
                "1 1 1".split(),
                "0 1 0".split(),
                "1 1 1".split(),
            ],
            1
        ],
        [
            [],
            0
        ],
        [
            [[]],
            0
        ],
        [
            [
                "1 0 1 1 1".split(),
                "1 0 1 0 1".split(),
                "1 1 1 0 1".split()
            ],
            1
        ]
    ]
    s = Solution()
    for test in tests:
        res = s.numIslands(test[0])
        if test[1] != res:
            print("Error. Got {} Wanted {}".format(res, test[1]))

    print("Completed")


