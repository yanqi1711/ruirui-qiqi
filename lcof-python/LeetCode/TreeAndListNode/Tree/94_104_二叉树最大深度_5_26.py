# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 0
        def dfs(root, curDepth):
            if not root:
                return None
            nonlocal depth
            depth = max(depth, curDepth)
            dfs(root.left, curDepth+1)
            dfs(root.right, curDepth+1)
        dfs(root, 1)
        return depth