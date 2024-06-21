# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deep(self,root):
        if not root:
            return 0
        # 找左边深度
        left = self.deep(root.left)
        # 如果已经存在深度差>1
        if left < 0:
            return -1
        right = self.deep(root.right)
        if right < 0:
            return -1
        return -1 if abs(left-right)>1 else 1+max(left,right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.deep(root) != -1