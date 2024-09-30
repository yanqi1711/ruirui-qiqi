from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        ans = float('inf')
        # 根据题意 root是最小的结点 所以需要dfs遍历找到第二大的
        def dfs(r):
            nonlocal ans
            if not r:
                return
            dfs(r.left)
            dfs(r.right)
            # 大于最小值root.val 才有资格更新 因为有相等的
            if r.val > root.val:
                ans = min(ans, r.val)
                return

        dfs(root)
        return ans if ans != float('inf') else -1
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