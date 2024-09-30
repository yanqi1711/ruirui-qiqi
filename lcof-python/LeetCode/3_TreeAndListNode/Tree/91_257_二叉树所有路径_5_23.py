class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        ans = []
        def dfs(root, curStr):
            nonlocal ans
            if root.left is None and root.right is None:
                ans.append(curStr)
                return
            if root.left:
                dfs(root.left,  curStr + "->" + str(root.left.val))
            if root.right:
                dfs(root.right, curStr + "->" + str(root.right.val))
        dfs(root, str(root.val))
        return ans