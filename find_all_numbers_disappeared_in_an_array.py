"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

Difficulty:Easy

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_len = len(nums)
        if not nums_len:
            return []

        a_pointer = 0
        while a_pointer < nums_len:
            if nums[a_pointer] == a_pointer + 1 or nums[a_pointer] == 0:
                a_pointer += 1
            elif nums[a_pointer] == nums[nums[a_pointer] - 1]:
                nums[a_pointer] = 0
                a_pointer += 1
            else:
                pos = nums[a_pointer] - 1
                nums[a_pointer], nums[pos] = nums[pos], nums[a_pointer]

        res = []
        for i in range(nums_len):
            if nums[i] == 0:
                res.append(i+1)

        return res


if __name__ == "__main__":
    s = Solution()
    assert s.findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5, 6]

    print("Completed")

