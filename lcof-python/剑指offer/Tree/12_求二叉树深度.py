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
# @return int整型
#
class Solution:
    def TreeDepth(self , pRoot: TreeNode) -> int:
        # write code here
        if not pRoot:
            return 0
        
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1