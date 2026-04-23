# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # dfs
        def dfs(root) -> list:
            
            if root is None:
                # 没有 所以偷和不偷都是0
                return [0,0]
            result = [0, 0]
            # 偷左边的结点 返回一个[] 下标为0是不偷， 1是偷时候的最大值
            left = dfs(root.left)
            right = dfs(root.right)
            # 不偷当前结点,那么就要偷两个儿子结点的最大值 然后相加
            result[0] = max(left[0], left[1]) + max(right[0], right[1])
            # 偷当前结点 就不能偷儿子结点 所以加0
            result[1] = left[0] + right[0] + root.val
            return result
        return max(dfs(root))