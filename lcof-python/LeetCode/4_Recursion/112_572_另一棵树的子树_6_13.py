# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, Root, subRoot):
        if Root is None and subRoot is None:
            return True
        if not Root and subRoot or Root and not subRoot or Root.val != subRoot.val:
            return False
        return self.check(Root.left, subRoot.left) and self.check(Root.right, subRoot.right)
    def dfs(self, Root, subRoot):
        if Root is None:
            return False
        # 检查当前节点是否符合,检查左子树是否符合,检查右子树是否符合
        return self.check(Root, subRoot) or self.dfs(Root.left, subRoot) or self.dfs(Root.right, subRoot)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)