# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 有根节点 就是1-1=0个
        ans = 1
        def dfs(root):
            if not root:
                return 0
            L = dfs(root.left)
            R = dfs(root.right)
            nonlocal ans
            ans = max(ans, L+R+1)
            # 返回左右两边最大的那一个
            return max(L,R)+1
        dfs(root)
        return ans-1