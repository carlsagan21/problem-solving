# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import math


class Solution:
    min_gap = math.inf
    prev = -math.inf

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left:
            self.minDiffInBST(root.left)

        gap = root.val - self.prev
        if gap < self.min_gap:
            self.min_gap = gap

        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.min_gap
