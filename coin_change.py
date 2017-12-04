"""
https://leetcode.com/problems/coin-change/description/

Difficulty:Medium

 You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
"""

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount <= 0:
            return 0
        if len(coins) == 0:
            return -1

        if amount in coins:
            return 1

        coins.sort()
        q = set()

        checked_amounts = set()
        for coin in coins:
            if amount > coin:
                q.add(amount - coin)
                checked_amounts.add(amount - coin)
        cnt = 1

        while len(q):
            next_q = set()
            for cur_amount in q:
                if cur_amount == 0:
                    return cnt

                for coin in coins:
                    if cur_amount == coin:
                        return cnt + 1
                    elif cur_amount > coin and (cur_amount - coin) not in checked_amounts:
                        next_q.add(cur_amount - coin)
                        checked_amounts.add(cur_amount - coin)

            q = next_q
            cnt += 1

        return -1


if __name__ == "__main__":
    tests = [
        [
            [1, 2, 5],
            11,
            3
        ],
        [
            [1, 2, 5],
            10,
            2,
        ],
        [
            [1, 2, 5],
            100,
            20,
        ],
        [
            [2],
            3,
            -1
        ],
        [
            [474, 83, 404, 3],
            264,
            8
        ],
        [
            [346, 29, 395, 188, 155, 109],
            9401,
            26
        ]
    ]
    s = Solution()
    for test in tests:
        res = s.coinChange(test[0], test[1])
        if test[2] != res:
            print("Inputs {}, {} Got {} Wanted {}".format(test[0], test[1], res, test[2]))

    print("Completed")



