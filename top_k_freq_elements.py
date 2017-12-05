"""
https://leetcode.com/problems/top-k-frequent-elements/discuss/

Difficulty:Medium

 Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""

import queue


class Solution_1(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        int_map = {}
        for num in nums:
            int_map[num] = int_map.get(num,0) + 1

        pq = queue.PriorityQueue()
        for key, val in int_map.items():
            pq.put((-1 * val, key))

        res = []
        while k > 0:
            item = pq.get()
            res.append(item[1])
            k -= 1

        return res


from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = Counter(nums)
        return [item[0] for item in c.most_common(k)]


if __name__ == "__main__":
    tests = [
        [
            [1,1,2,1,2,4],
            2,
            [1,2]
        ],
        [
            [1, 1, 2, 1, 2, 4],
            1,
            [1]
        ],
        [
            [3,3,3,1, 1, 3, 2, 1, 2, 4],
            2,
            [3, 1]
        ],
        [
            [3, 3, 3, 1, 1, 3, 2, 1, 2, 4],
            3,
            [3, 1, 2]
        ]
    ]

    s = Solution()
    for test in tests:
        res = s.topKFrequent(test[0], test[1])
        if test[2] != res:
            print("Inputs {}, {} Got {} Wanted {}".format(test[0], test[1], res, test[2]))

    print("Completed")