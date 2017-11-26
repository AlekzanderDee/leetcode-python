"""
Difficulty:Medium

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""


class Solution:
    def binary_extreme_search(self, array, target, left_extreme=True):
        array_len = len(array)
        low, high = 0, array_len - 1
        while low < high:
            mid = (low + high) // 2
            if array[mid] == target:
                if left_extreme and mid > 0:
                    if array[mid - 1] == target:
                        high = mid - 1
                    else:
                        return mid
                elif not left_extreme and mid < array_len - 1:
                    if array[mid + 1] == target:
                        low = mid + 1
                    else:
                        return mid
                else:
                    return mid
            elif array[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        if array[low] == target:
            return low

        return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        left_index = self.binary_extreme_search(nums, target, left_extreme=True)
        right_index = self.binary_extreme_search(nums, target, left_extreme=False)

        return [left_index, right_index]


if __name__ == "__main__":
    tests = [
        [[5, 7, 7, 8, 8, 10], 8, [3, 4]],
        [[5, 7, 7, 8, 8, 10], 7, [1, 2]],
        [[1, 2, 3, 4, 5, 5, 5, 6], 5, [4, 6]],
        [[1, 2, 3, 4, 5, 5, 5, 6], 9, [-1, -1]],
        [[9], 19, [-1, -1]],
        [[], 19, [-1, -1]],
    ]

    s = Solution()
    for test in tests:
        res = s.searchRange(test[0], test[1])
        if res != test[2]:
            print("Error. input ({}, {}) wanted {} got {}".format(test[0], test[1], test[2], res))

    print("completed")
