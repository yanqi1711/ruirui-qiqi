class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pRoot TreeNode类 
# @return TreeNode类
#
class Solution:
    def Mirror(self , pRoot: TreeNode) -> TreeNode:
        # write code here
        if not pRoot:
            return None
        # 先交换 
        pRoot.left, pRoot.right = pRoot.right, pRoot.left

        self.Mirror(pRoot.left)
        self.Mirror(pRoot.right)
        return pRoot