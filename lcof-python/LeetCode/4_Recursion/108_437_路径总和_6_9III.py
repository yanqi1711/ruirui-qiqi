# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


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
        """
        Calculate the number of paths in the binary tree rooted at 'root' that sum up to 'targetSum'.

        Args:
            root: The root of the binary tree.
            targetSum: The target sum to be achieved.

        Returns:
            The number of paths that sum up to the target sum.
        """
        if not root:
            return 0
        self.preorder(root, targetSum)
        return self.count