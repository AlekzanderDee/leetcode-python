"""
Difficulty:Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums_len = len(nums)
        if nums_len < 2:
            if target in nums:
                return 0
            return -1

        low, high = 0, nums_len - 1
        # find the pivot element
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[-1]:
                low = mid + 1
            else:
                high = mid - 1

        # decide in which part od rotated array we should search
        if target == nums[low]:
            return low
        elif target > nums[-1]:
            high = low
            low = 0
        else:
            low = low
            high = nums_len - 1

        # final binary search in part of the array
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        if nums[low] == target:
            return low

        return -1


if __name__ == "__main__":
    tests = [
        [[4, 5, 6, 7, 0, 1, 2], 0, 4],
        [[4, 5, 6, 7, 0, 1, 2], 5, 1],
        [[4, 5, 6, 7, 0, 1, 2], 2, 6],
        [[4, 5, 6, 7, 0, 1, 2], 1, 5],
        [[4, 5, 6, 7, 0, 1, 2], 4, 0],
        [[], 5, -1],
        [[4, 6], 5, -1],
        [[1,], 0, -1],
        [[3, 1], 0, -1],

    ]
    s = Solution()
    for test in tests:
        res = s.search(test[0], test[1])
        if res != test[2]:
            print("Error. input ({}, {}) wanted {} got {}".format(test[0], test[1], test[2], res))

    print("completed")
