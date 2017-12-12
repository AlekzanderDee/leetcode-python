"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

Difficulty:Medium

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

"""


class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                res.append(index + 1)
            else:
                nums[index] *= -1
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]
    assert s.findDuplicates([1, 3, 4, 3]) == [3]

    print("Completed")
