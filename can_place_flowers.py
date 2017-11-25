"""
Difficulty:Easy

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

Note:

    The input array won't violate no-adjacent-flowers rule.
    The input array size is in the range of [1, 20000].
    n is a non-negative integer which won't exceed the input array size.

"""


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        bed_len = len(flowerbed)

        # edge case
        if bed_len == 1 and flowerbed[0] == 0 and n <= 1:
            return True

        dp = [0] * bed_len

        for ind in range(bed_len):
            if flowerbed[ind] == 1:
                dp[ind] = 0
            else:
                # edge case
                if ind == 0:
                    dp[ind] = 0 if flowerbed[ind] == 1 or flowerbed[ind + 1] == 1 else 1
                # edge case
                elif ind == bed_len - 1:
                    dp[ind] = 0 if flowerbed[ind] == 1 or flowerbed[ind - 1] == 1 or dp[ind - 1] == 1 else 1
                # common case
                else:
                    if sum((flowerbed[ind - 1], flowerbed[ind], flowerbed[ind + 1], dp[ind - 1])) == 0:
                        dp[ind] = 1
                    else:
                        dp[ind] = 0

        return sum(dp) >= n


if __name__ == "__main__":
    tests = [
        {
            "flowerbed": [1, 0, 0, 0, 1],
            "n": 1,
            "output": True
        },
        {
            "flowerbed": [1, 0, 0, 0, 1],
            "n": 2,
            "output": False
        },
        {
            "flowerbed": [1, 0, 0, 0, 0, 1],
            "n": 2,
            "output": False
        },
        {
            "flowerbed": [1, 0, 1, 0, 1, 0, 1],
            "n": 1,
            "output": False
        },
        {
            "flowerbed": [0, 0, 1, 0, 1],
            "n": 1,
            "output": True
        },
        {
            "flowerbed": [0, 0],
            "n": 2,
            "output": False
        },
    ]

    s = Solution()
    for test in tests:
        res = s.canPlaceFlowers(test["flowerbed"], test["n"])
        if res != test["output"]:
            print("Error. input ({}, {}) wanted {} got {}".format(test["flowerbed"], test["n"], test["output"], res))

    print("completed")
