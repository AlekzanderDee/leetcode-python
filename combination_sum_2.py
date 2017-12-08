"""
https://leetcode.com/problems/combination-sum-ii/description/

Difficulty:Medium

 Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:

[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

"""

class Solution:
    def dfs(self, target, start, candidates, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            self.dfs(target-candidates[i], i + 1, candidates, path + [candidates[i]], res)

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(target, 0, candidates, [], res)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
