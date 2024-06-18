# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def popreorder(self, root, sum):
        if not root:
            return sum
        rightSum = self.popreorder(root.right, sum)
        root.val += rightSum
        leftSum=self.popreorder(root.left,root.val);
        return leftSum

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sum = 0
        self.popreorder(root, sum)
        return root