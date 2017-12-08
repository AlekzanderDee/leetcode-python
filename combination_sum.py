"""
https://leetcode.com/problems/combination-sum/description/

Difficulty:Medium

 Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:

[
  [7],
  [2, 2, 3]
]

"""

import queue

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not len(candidates):
            return []

        candidates.sort()

        res = set()
        q = queue.Queue()
        q.put(([], target))

        while not q.empty():
            item = q.get()
            val = item[1]

            for c in candidates:
                path = item[0][:]
                path.append(c)
                if val == c:
                    res.add(tuple(sorted(path)))
                elif val > c:
                    q.put((path, val - c))
                else:
                    break

        return [[item for item in combination] for combination in res]


class Solution2:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res)

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))
    print(s.combinationSum([], 7))
    print(s.combinationSum([92,71,89,74,102,91,70,119,86,116,114,106,80,81,115,99,117,93,76,77,111,110,75,104,95,112,94,73], 310))
