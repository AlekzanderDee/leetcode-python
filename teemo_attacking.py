"""
Difficulty:Medium

n LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.

Example 1:

Input: [1,4], 2
Output: 4
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned immediately.
This poisoned status will last 2 seconds until the end of time point 2.
And at time point 4, Teemo attacks Ashe again, and causes Ashe to be in poisoned status for another 2 seconds.
So you finally need to output 4.

Example 2:

Input: [1,2], 2
Output: 3
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned.
This poisoned status will last 2 seconds until the end of time point 2.
However, at the beginning of time point 2, Teemo attacks Ashe again who is already in poisoned status.
Since the poisoned status won't add up together, though the second poisoning attack will still work at time point 2, it will stop at the end of time point 3.
So you finally need to output 3.

Note:

    You may assume the length of given time series array won't exceed 10000.
    You may assume the numbers in the Teemo's attacking time series and his poisoning time duration per attacking are non-negative integers, which won't exceed 10,000,000.

"""


class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        attacks_cnt = len(timeSeries)
        if attacks_cnt == 0:
            return 0

        attack_lengths = []
        current_attack = [timeSeries[0], timeSeries[0] + duration]
        for attack_ind in range(1, attacks_cnt):
            if current_attack[1] > timeSeries[attack_ind]:
                current_attack[1] = timeSeries[attack_ind] + duration
            else:
                attack_lengths.append(current_attack[1] - current_attack[0])
                current_attack = [timeSeries[attack_ind], timeSeries[attack_ind] + duration]

        attack_lengths.append(current_attack[1] - current_attack[0])

        return sum(attack_lengths)


if __name__ == "__main__":
    tests = [
        [[1, 4], 2, 4],
        [[1, 2], 2, 3],
        [[1, 2, 5], 2, 5],
    ]

    s = Solution()
    for test in tests:
        res = s.findPoisonedDuration(test[0], test[1])
        if res != test[2]:
            print("Error. input ({}, {}) wanted {} got {}".format(test[0], test[1], test[2], res))

    print("completed")
