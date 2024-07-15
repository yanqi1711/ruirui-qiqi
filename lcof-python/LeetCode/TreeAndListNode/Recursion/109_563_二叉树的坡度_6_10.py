# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root:
            return 0
        return root.val + self.dfs(root.left) + self.dfs(root.right)
    
    def getValue(self, root):
        if not root:
            return 0
        cur = abs(self.dfs(root.left)- self.dfs(root.right))
        left = self.getValue(root.left)
        right = self.getValue(root.right)
        return cur + left + right

    def findTilt(self, root: Optional[TreeNode]) -> int:
        return self.getValue(root)
# 更快   
# class Solution:
#     def __init__(self):
#         self.ans = 0
    
#     def getValue(self, root):
#         if not root:
#             return 0
#         left = self.getValue(root.left)
#         right = self.getValue(root.right)
#         self.ans += abs(left - right)
#         return root.val + left + right

#     def findTilt(self, root: Optional[TreeNode]) -> int:
#         self.getValue(root)
#         return self.ans