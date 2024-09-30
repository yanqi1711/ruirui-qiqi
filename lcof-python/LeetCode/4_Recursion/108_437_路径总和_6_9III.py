# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0

    def preorder(self, root, targetSum):
        if not root: return 
        self.SumCount(root, targetSum)
        self.preorder(root.left, targetSum)
        self.preorder(root.right, targetSum)

    def SumCount(self, root, targetSum):
        if not root:
            return
        if targetSum - root.val == 0:
            self.count += 1
        self.SumCount(root.left, targetSum- root.val)
        self.SumCount(root.right, targetSum- root.val)     
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        self.preorder(root, targetSum)
        return self.count