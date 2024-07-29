# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 和二叉树直径一样 但是这里面要求val必须相等 不相等长度就是0
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # 有根节点 就是1-1=0个
        ans = 1
        def dfs(root):
            if not root:
                return 0
            # 寻找左右两边的最大长度
            L = dfs(root.left)
            R = dfs(root.right)
            # 重置长度 如果val不相等 长度就是0 但是最大长度是被ans记录的
            L = L if root.left and root.val == root.left.val else 0
            R = R if root.right and root.val == root.right.val else 0
            nonlocal ans
            ans = max(ans, L+R+1)
            # 返回左右两边最大的那一个
            return max(L,R)+1
        dfs(root)
        return ans-1