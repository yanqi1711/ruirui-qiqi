# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
# 这个题dfs更好
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node, height):
            if node is None:
                return
            # 第一次先把数最左边的数加入列表
            if height == len(ans):
                ans.append(node.val)
            # 回溯的时候会走这里根据高度(在这里也就是索引，第一层为0 正好对应空 高度0，第二层索引为1刚好对应高度1)
            else:
                ans[height]  = max(ans[height], node.val)
            dfs(node.left, height + 1)
            dfs(node.right, height + 1)
        dfs(root, 0)
        return ans

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        # 结果
        ans = []
        # 存放层级结点的列表
        curLayer = []
        while q:
            # 每一层重置
            curLayer = []
            curVal = float('-inf')
            while q:
                node = q.popleft()
                if node.left:
                    curLayer.append(node.left)
                if node.right:
                    curLayer.append(node.right)
                curVal = max(curVal, node.val)
            ans.append(curVal)
            q = deque(curLayer)
        return ans

            
            