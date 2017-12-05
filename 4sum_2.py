"""
https://leetcode.com/problems/4sum-ii/discuss/

Difficulty:Medium

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

"""


class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ab_sum_map = {}
        for a_item in A:
            for b_item in B:
                ab_sum_map[-1 * (a_item + b_item)] = ab_sum_map.get(-1 * (a_item + b_item), 0) + 1

        cnt = 0
        for c_item in C:
            for d_item in D:
                cnt += ab_sum_map.get(c_item+d_item, 0)

        return cnt


if __name__ == "__main__":
    tests = [
        [
            [1, 2],
            [-2, -1],
            [-1, 2],
            [0, 2],
            2
        ],
        [
            [-1, -1],
            [-1, 1],
            [-1, 1],
            [1, -1],
            6
        ]
    ]
    s = Solution()
    for test in tests:
        for test in tests:
            res = s.fourSumCount(test[0], test[1], test[2], test[3])
            if test[4] != res:
                print("Inputs {}, {}, {}, {} Got {} Wanted {}".format(test[0], test[1], test[2], test[3], res, test[4]))

    print("Completed")
