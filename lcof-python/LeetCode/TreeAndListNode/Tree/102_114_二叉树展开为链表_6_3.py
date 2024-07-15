# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 重点 inplace 原地修改
        def helper(node):
            if not node:
                return None
            # 获得的结点都是最后的
            left = helper(node.left)
            right = helper(node.right)
            # 如何扁平 把左子树连接到右边 左边为None 右边连接在左节点的右节点
            # 因为是递归 一定会在叶子结点的父结点-> 其左结点是叶子节点所以leftChild.right = None
            # 开始扁平 所以一定会从底层向上层一次扁平 
            # 即使多次递归 left.right也一定是None 因为左边的子树从底层就开始送到右子树了
            if left:
                left.right = node.right
                node.right = node.left
                node.left = None
            # 1:全是右子树 当然直接返回right_end  2:左右两边都有也直接返回right
            # 重点: 3:全是左子树->返回left 因为以上操作并没修改right 返回right会成为None 
            # 4:都没有就是叶子结点 返回叶子节点
            # 返回的都是最后一个节点
            return right or left or node
        helper(root)