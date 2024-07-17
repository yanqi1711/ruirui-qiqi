class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Counter, Optional


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        cnt = Counter()
        def dfs(root):
            if not root:
                return 0
            sum = root.val + dfs(root.left) + dfs(root.right)
            cnt[sum] +=1
            return sum
        dfs(root)
        maxCnt = max(cnt.values())
        return [s for s,c in cnt.items() if c == maxCnt]