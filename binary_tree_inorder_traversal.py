"""
https://leetcode.com/problems/binary-tree-inorder-traversal/description/

Difficulty:Medium

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],

   1
    \
     2
    /
   3

return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution2:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        expanded_nodes = set()
        resulting_list = [root,]
        while True:
            changed = False
            for ind, node in enumerate(resulting_list):
                if node not in expanded_nodes and node is not None:
                    expanded_nodes.add(node)
                    if node.left or node.right:
                        changed = True
                        resulting_list = resulting_list[:ind] + [node.left, node, node.right] + resulting_list[ind+1:]
                        break
            if not changed:
                break
        return [node.val for node in resulting_list if node is not None]


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes_stack = []
        res = []
        cur = root
        while cur is not None or nodes_stack:
            while cur is not None:
                nodes_stack.append(cur)
                cur = cur.left

            cur = nodes_stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    s = Solution()
    print(s.inorderTraversal(root))



