class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # [] 是因为需要一个可迭代对象
        q = deque([root])
        while q:
            node = q.popleft()
            # 必须先right后left 因为要找左下角的值,所以右边先入队列 这样就能保证左边一定是后面出来的
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
            ans = node.val
        return ans
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # 当前最高高度以及值
        curVal = curHeight = 0
        def dfs(root,height):
            if not root:
                return
            # 每次增加高度
            height+=1
            dfs(root.left, height)
            dfs(root.right, height)
            nonlocal curVal,curHeight
            # 记录深的结点 所以第一层的height=1 会被下面更高的高度屏蔽
            if height > curHeight:
                curHeight = height
                curVal = root.val
        dfs(root, 0)
        return curVal