class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param root TreeNode类 
# @param sum int整型 
# @return bool布尔型
#
class Solution:
    def hasPathSum(self , root: TreeNode, sum: int) -> bool:
        # write code here
        if not root:
            return False
        sum = sum - root.val
        # 必须是叶子结点
        if sum == 0 and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right, sum)