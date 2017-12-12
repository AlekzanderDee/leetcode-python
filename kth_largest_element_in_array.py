"""
https://leetcode.com/problems/kth-largest-element-in-an-array/description/


Difficulty:Medium

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

import heapq

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or k > len(nums):
            return

        h = [-1 * num for num in nums]
        heapq.heapify(h)
        item = None
        while k > 0:
            item = heapq.heappop(h)
            k -= 1

        return -1 * item


if __name__ == "__main__":
    tests = [
        [
            [-1, -1],
            2,
            -1
        ],
        [
            [4,3,1,2,6,5],
            2,
            5
        ]
    ]
    s = Solution()
    for test in tests:
        res = s.findKthLargest(test[0], test[1])
        if test[2] != res:
            print("Inputs {}, {} Got {} Wanted {}".format(test[0], test[1], res, test[2]))

    print("Completed")

