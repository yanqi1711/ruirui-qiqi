class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param preOrder int整型一维数组 
# @param vinOrder int整型一维数组 
# @return TreeNode类
#
class Solution:
    def reConstructBinaryTree(self , preOrder: List[int], vinOrder: List[int]) -> TreeNode:
        # write code here
        if not preOrder or not vinOrder:
            return None
        m = len(preOrder)
        n = len(vinOrder)
        root = TreeNode(preOrder[0])
        for i in range(n):
            if vinOrder[i] == preOrder[0]:
                # 前序左子树
                pre = preOrder[1:i+1]
                # 中序
                vin = vinOrder[:i]
                # 递归重建左子树
                root.left = self.reConstructBinaryTree(preOrder=pre,vinOrder=vin)

                # 前序右子树
                pre = preOrder[i+1:]
                # 中序
                vin = vinOrder[i+1:]
                # 递归重建右子树
                root.right = self.reConstructBinaryTree(pre,vin)
        return root