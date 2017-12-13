"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

Difficulty:Hard

 Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3

Return 6.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.sum_down(root)

        return self.max_sum

    def sum_down(self, node):
        if not node:
            return 0

        left = max((0, self.sum_down(node.left)))
        right = max((0, self.sum_down(node.right)))
        self.max_sum = max([self.max_sum, node.val + left + right])
        # the upper node can build the path with the largest path so far
        return node.val + max((left, right))









