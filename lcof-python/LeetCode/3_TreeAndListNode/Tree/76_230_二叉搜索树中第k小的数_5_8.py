# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        self.ans = []
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            self.ans.append(root.val)
            dfs(root.right)
        dfs(root)
        return self.ans[k-1]