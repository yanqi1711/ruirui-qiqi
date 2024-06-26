from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        ans = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
            return
        dfs(root)
        # .sort()会返回None
        ans = list(set(ans))
        ans.sort()
        print(ans)
        return -1 if len(ans) <= 1 else ans[1]