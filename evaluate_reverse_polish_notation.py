"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

Difficulty:Medium

 Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

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


if __name__ == "__main__":
    tests = [
        [
            ["2", "1", "+", "3", "*"],
            9
        ],
        [
            ["4", "13", "5", "/", "+"],
            6
        ],
        [
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
            22
        ]
    ]
    s = Solution()
    for test in tests:
        res = s.evalRPN(test[0])
        if res != test[1]:
            print("Error. Expression {}; result expected {}, got {}".format(test[0], test[1], res))

    print("Completed")

