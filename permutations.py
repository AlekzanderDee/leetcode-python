"""
Difficulty:Medium

 Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 2:
            return [nums]

        perms = []
        for ind, num in enumerate(nums):
            sub_permutations = self.permute(nums[:ind] + nums[ind + 1:])
            for s in sub_permutations:
                perms.append([num] + s)

        return perms


if __name__ == "__main__":
    tests = [
        [[1, 2, 3], [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ]]
    ]

    s = Solution()

    for test in tests:
        res = s.permute(test[0])
        if res != test[1]:
            print("Error. input {} wanted {} got {}".format(test[0], test[1], res))

    print("completed")

