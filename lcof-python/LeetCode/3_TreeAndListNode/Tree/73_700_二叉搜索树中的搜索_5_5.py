class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        while root:
            if root.val == val:
                return root
            root = root.left if root.val > val else root.right
        return None
        """
        if not root:
            return None
        if root.val == val:
            print(root.val)
            return root
        elif val > root.val:
            return self.searchBST(root.right,val)
        else:
            return self.searchBST(root.left,val)