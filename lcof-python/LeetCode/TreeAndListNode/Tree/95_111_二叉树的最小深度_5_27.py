class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional

# 这个题 bfs更快
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        depth = 0
        while q:
            depth+=1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return depth

    # def minDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     depth = float("inf")
    #     def dfs(root, curDepth):
    #         if root is None:
    #             return
    #         dfs(root.left, curDepth+1)
    #         dfs(root.right, curDepth+1)
    #         nonlocal depth
    #         if root.left is None and root.right is None:
    #             depth = min(depth, curDepth)
    #     dfs(root, 1)
    #     return depth