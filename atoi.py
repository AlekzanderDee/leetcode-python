"""
Difficulty:Medium

mplement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.

spoilers alert... click to show requirements for atoi.
Requirements for atoi:

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

"""

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        number = 0
        numbers_map = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }
        # remove whitespace around
        str = str.strip()
        str_len = len(str)
        if str_len == 0:
            return number

        first_index = 0

        number_sign = 1
        if str[0] in ["-", "+"]:
            first_index += 1
            number_sign = 1 if str[0] == "+" else -1

        last_index = first_index
        number_list = []

        while last_index < str_len:
            if str[last_index] in numbers_map:
                number_list.append(numbers_map[str[last_index]])
                last_index += 1
            else:
                break

        tens_power = len(number_list) - 1
        for num in number_list:
            number += num * pow(10, tens_power)
            tens_power -= 1

        number = int(number_sign * number)
        if number > 2147483647:
            number = 2147483647
        elif number < -2147483648:
            number = -2147483648

        return number


if __name__ == "__main__":
    tests = [
        ["   42  ", 42],
        ["   -42  ", -42],
        ["   42asd dasd ", 42],
        ["-999  ", -999],
        ["999  ", 999],
        ["999", 999],

    ]
    s = Solution()

    for test in tests:
        res = s.myAtoi(test[0])
        if res != test[1]:
            print("Error. input \"{}\" wanted {} got {}".format(test[0], test[1], res))

    print("completed")





