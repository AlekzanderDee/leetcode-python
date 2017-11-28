"""
https://leetcode.com/problems/largest-number/description/

Difficulty:Medium

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
Note: The result may be very large, so you need to return a string instead of an integer.
"""


from functools import cmp_to_key


class SolutionLowLevel:

    @staticmethod
    def cmp(x, y):
        if len(x) == len(y) and x[0] != y[0]:
            return ord(x[0]) - ord(y[0])

        if len(x) != len(y) and x[0] != y[0]:
            return ord(x[0]) - ord(y[0])

        if len(x) == len(y) and x[0] == y[0]:
            for ind in range(len(x)):
                if x[ind] != y[ind]:
                    return ord(x[ind]) - ord(y[ind])
            return 0

        if len(x) != len(y) and x[0] == y[0]:
            x_ind = y_ind = 0
            while True:
                if x_ind >= len(x) and y_ind >= len(y):
                    return ord(x[-1]) - ord(y[-1])

                if x_ind >= len(x):
                    x_val = x[0]
                else:
                    x_val = x[x_ind]

                if y_ind >= len(y):
                    y_val = y[0]
                else:
                    y_val = y[y_ind]

                if x_val != y_val:
                    return ord(x_val) - ord(y_val)
                x_ind += 1
                y_ind += 1

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        str_list = [str(num) for num in nums]

        return ''.join(sorted(str_list, key=cmp_to_key(self.cmp), reverse=True)).lstrip("0") or "0"



class Solution:

    @staticmethod
    def cmp(x, y):
        option_1 = x + y
        option_2 = y + x
        if option_1 > option_2:
            return 1
        elif option_1 == option_2:
            return 0
        return -1

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        str_list = [str(num) for num in nums]

        return ''.join(sorted(str_list, key=cmp_to_key(self.cmp), reverse=True)).lstrip("0") or "0"


if __name__ == "__main__":
    tests = [
        [
            [3, 30, 34, 5, 9],
            "9534330"
        ],
        [
            [121, 12],
            "12121"
        ],
        [
            [0, 0],
            "0"
        ],
        [
            [0, 1, 0],
            "100"
        ],
        [
            [9051, 5526, 2264, 5041, 1630, 5906, 6787, 8382, 4662, 4532, 6804, 4710, 4542, 2116, 7219, 8701, 8308, 957,
             8775, 4822, 396, 8995, 8597, 2304, 8902, 830, 8591, 5828, 9642, 7100, 3976, 5565, 5490, 1613, 5731, 8052,
             8985, 2623, 6325, 3723, 5224, 8274, 4787, 6310, 3393, 78, 3288, 7584, 7440, 5752, 351, 4555, 7265, 9959,
             3866, 9854, 2709, 5817, 7272, 43, 1014, 7527, 3946, 4289, 1272, 5213, 710, 1603, 2436, 8823, 5228, 2581, 771,
             3700, 2109, 5638, 3402, 3910, 871, 5441, 6861, 9556, 1089, 4088, 2788, 9632, 6822, 6145, 5137, 236, 683,
             2869, 9525, 8161, 8374, 2439, 6028, 7813, 6406, 7519],
            "995998549642963295795569525905189958985890288238775871870185978591838283748308830827481618052787813771758475"
            "2775197440727272657219710710068616836822680467876406632563106145602859065828581757525731563855655526549054415"
            "2285224521351375041482247874710466245554542453243428940883976396394639103866372337003513402339332882869278827"
            "0926232581243924362362304226421162109163016131603127210891014"
        ]

    ]
    s = Solution()
    for test in tests:
        res = s.largestNumber(test[0])
        if res != test[1]:
            print("Error: input {}; wanted {} got {}".format(test[0], test[1], res))

    print("completed")
