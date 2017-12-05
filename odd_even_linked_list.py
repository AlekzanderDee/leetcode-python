"""
https://leetcode.com/problems/odd-even-linked-list/description/

Difficulty:Medium

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking
about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def from_list(cls, nums):
        fake_head = cls(0)
        h = fake_head
        for num in nums:
            h.next = cls(num)
            h = h.next

        return fake_head.next

    def to_list(self):
        l = []
        h = self
        while h != None:
            l.append(h.val)
            h = h.next
        l.append(None)

        return l


class Solution_1:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None:
            return head
        fake_head = ListNode(0)
        fake_head.next = head
        h = head
        p = head

        p_distance = 2

        while True:
            for _ in range(p_distance):
                p = p.next
                if p is None:
                    return fake_head.next

            even_head = h.next
            even_tail = even_head
            while even_tail.next != p:
                even_tail = even_tail.next

            h.next = p
            even_tail.next = p.next
            p.next = even_head

            if even_tail.next is None:
                break

            p_distance += 1
            h = p

        return fake_head.next


class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None:
            return head

        odd_tail = head
        even_head = head.next
        even_tail = even_head

        while even_tail is not None and even_tail.next is not None:
            odd_tail.next = even_tail.next
            odd_tail = odd_tail.next

            even_tail.next = odd_tail.next
            even_tail = even_tail.next

        odd_tail.next = even_head

        return head


if __name__ == "__main__":
    tests = [
        [
            [1],
            [1, None]
        ],
        [
            [1, 2],
            [1, 2, None]
        ],
        [
            [1, 2, 3],
            [1, 3, 2, None]
        ],
        [
            [1, 2, 3, 4, 5, 6],
            [1, 3, 5, 2, 4, 6, None]
        ],
        [
            [1, 2, 3, 4, 5, 6, 7],
            [1, 3, 5, 7, 2, 4, 6, None]
        ]
    ]
    s = Solution()
    for test in tests:
        res = s.oddEvenList(ListNode.from_list(test[0]))
        res_list = res.to_list()
        if test[1] != res_list:
            print("Input {} Got {} Wanted {}".format(test[0], res_list, test[1]))

    print("Completed")
