class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pRoot1 TreeNode类 
# @param pRoot2 TreeNode类 
# @return bool布尔型
#
class Solution:
    def isSame(self, pRoot1, pRoot2):
         if not pRoot2: return True
         if not pRoot1 or pRoot1.val != pRoot2.val: return False
         return self.isSame(pRoot1.left, pRoot2.left) and self.isSame(pRoot1.right, pRoot2.right)
        
    def HasSubtree(self , pRoot1: TreeNode, pRoot2: TreeNode) -> bool:
        # write code here
        if not pRoot2:
            return False
        if pRoot1 is None and pRoot2 is not None:
            return False
        if pRoot2 is None and pRoot1 is None:
            return True
        return self.isSame(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)