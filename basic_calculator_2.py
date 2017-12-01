"""
https://leetcode.com/problems/basic-calculator-ii/description/

Difficulty:Medium

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:

"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5

Note: Do not use the eval built-in library function.
"""
import operator

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operands_stack = []

        def my_div(a, b):
            # here take care of the case like "1/-22",
            # in Python it returns -1, while in
            # Leetcode it should return 0
            if a * b < 0 and a % b != 0:
                return a // b + 1
            else:
                return a // b

        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": my_div,
        }

        for item in tokens:
            if not item in operators:
                operands_stack.append(int(item))
            else:
                x = operands_stack.pop()
                y = operands_stack.pop()
                operands_stack.append(operators[item](y, x))

        return operands_stack.pop()

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operator_rangs = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }
        for op in operator_rangs:
            s = s.replace(op, " {} ".format(op))

        postfix = []
        buf = []
        expression_list = [element.strip() for element in s.split()]

        for item in expression_list:
            if item not in operator_rangs:
                postfix.append(item)
            else:
                if not buf:
                    buf.append(item)
                else:
                    while buf and operator_rangs[item] <= operator_rangs[buf[-1]]:
                        postfix.append(buf.pop())
                    buf.append(item)
        while buf:
            postfix.append(buf.pop())

        return self.evalRPN(postfix)


if __name__ == "__main__":
    tests = [
        [
            "3+2*2",
            7
        ],
        [
            " 3/2 ",
            1
        ],
        [
            " 3+5 / 2 ",
            5
        ],
        [
            "6/3 + 4* 5 - 1",
            21
        ]
    ]
    s = Solution()
    for test in tests:
        res = s.calculate(test[0])
        if res != test[1]:
            print("Error. Expression {}; result expected {}, got {}".format(test[0], test[1], res))

    print("Completed")
