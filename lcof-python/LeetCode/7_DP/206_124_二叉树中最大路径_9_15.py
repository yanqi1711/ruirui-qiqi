# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 因为要求最大值 而这道题又存在负数所以必须要存储最大值变量 不能是0 因为必须选一个不然root = [-3]无法通过
        maxSum = root.val
        # 取就可以连接左右两边 不取就在左右2边比大小
        def dfs(root): # 后序遍历 因为当前结点最大最小值需要下面结点的最大值的状态
            if not root:
                return 0
            # 最大贡献值大于 0 时，才会选取对应子节点
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            # 不再向上走了 因为父结点可能是负数 所以相当于减枝,把当前结点当根结点 从左往右走一遍(题目要求 每隔结点只能用一次)
            current_root = root.val + left + right
            nonlocal maxSum
            maxSum = max(current_root, maxSum)
            # 向上走找所有情况， 为了最大值 所以只能选左右2边最大的那个 因为只能走一次 所以只能选左边或者右边
            return root.val + max(left, right)
        dfs(root)
        return maxSum