# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pRoot TreeNode类 
# @return bool布尔型
#
# class Solution:
#     # 计算该子树深度
#     def getdepth(self, root: TreeNode) -> int: 
#         if not root: # 空节点深度为0
#             return 0
#         # 递归计算当前root左右子树的深度差
#         left = self.getdepth(root.left) 
#         # 当前节点左子树不平衡,则该树不平衡
#         if left < 0: 
#             return -1
#         right = self.getdepth(root.right)
#         # 当前节点右子树不平衡,则该树不平衡
#         if right < 0: 
#             return -1 
#         return -1 if abs(left-right) > 1 else 1 + max([left, right])
    
#     def IsBalanced_Solution(self , pRoot: TreeNode) -> bool:
#         if not pRoot:
#             return True
#         return self.getdepth(pRoot) != -1

class Solution:
    def deep(self,root):
        if not root:
            return 0
        left = self.deep(root.left)
        right = self.deep(root.right)
        return max(left, right) + 1
    def IsBalanced_Solution(self , pRoot: TreeNode) -> bool:
        if not pRoot: return True

        left = self.deep(pRoot.left)
        right = self.deep(pRoot.right)

        if left - right > 1 or left - right < -1:
            return False

        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)