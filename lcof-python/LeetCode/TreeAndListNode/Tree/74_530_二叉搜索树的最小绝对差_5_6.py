# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return float("inf")
        self.prev = -float("inf")
        self.min_diff = float("inf")
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            # 左 中 右  1: 中-左 2: 右-中
            self.min_diff = min(self.min_diff, root.val-self.prev)
            self.prev = root.val
            dfs(root.right)
        dfs(root)
        return self.min_diff