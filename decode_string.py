"""
https://leetcode.com/problems/decode-string/description/

Difficulty:Medium

 Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

"""


class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        stack = []
        i = 0

        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        while i < len(s):
            if s[i] not in nums and s[i] not in ["[", "]"]:
                if len(stack) == 0:
                    res += s[i]
                else:
                    stack[-1][1] += s[i]

            elif s[i] in nums:
                num = s[i]
                while s[i+1] in nums:
                    num += s[i+1]
                    i += 1
                stack.append([int(num), ""])

            elif s[i] == "]":
                item = stack.pop()
                if len(stack) > 0:
                    stack[-1][1] += item[1] * item[0]
                else:
                    res += item[1] * item[0]
            i += 1
        return res


if __name__ == "__main__":
    tests = [
        [
            "3[a]2[bc]",
            "aaabcbc"
        ],
        [
            "3[a2[c]]",
            "accaccacc"
        ],
        [
            "2[abc]3[cd]ef",
            "abcabccdcdcdef"
        ],
        [
            "",
            "",
        ],
        [
            "ab11[2[a]I]",
            "abaaIaaIaaIaaIaaIaaIaaIaaIaaIaaIaaI"
        ]
    ]
    s = Solution()
    for test in tests:
        res = s.decodeString(test[0])
        if test[1] != res:
            print("Input {} Got {} Wanted {}".format(test[0], res, test[1]))

    print("Completed")