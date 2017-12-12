"""
https://leetcode.com/problems/sliding-window-maximum/description/

Difficulty:Hard

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        window_start, window_end, res = 0, k, []

        while window_end <= len(nums):
            window_max = max(nums[window_start:window_end])
            res.append(window_max)

            window_start += 1
            window_end += 1

        return res


if __name__ == "__main__":
    tests = [
        [
            [1, 3, -1, -3, 5, 3, 6, 7],
            3,
            [3, 3, 5, 5, 6, 7]
        ]
    ]
    s = Solution()
    for test in tests:
        res = s.maxSlidingWindow(test[0],test[1])
        if test[2] != res:
            print("Inputs ({}, {}) Got {} Wanted {}".format(test[0], test[1], res, test[2]))

    print("Completed")