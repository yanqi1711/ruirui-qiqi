# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return
        # 第一层
        if depth == 1:
            # 作为新的Root 左边是原来的旧结点
            return TreeNode(val, root, None)
        # 第二层
        if depth == 2:
            root.left = TreeNode(val, root.left, None)
            # 原本在右边就要挂到右边
            root.right = TreeNode(val, None, root.right)
        else: #其余情况 递归
            root.left = self.addOneRow(root.left, val, depth-1)
            root.right = self.addOneRow(root.right, val, depth-1)
        return root