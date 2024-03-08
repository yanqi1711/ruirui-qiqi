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
# @return int整型
#
class Solution:
    def __init__(self) -> None:
        self.count = 0

    # 任意一个遍历都行
    # 因为不需要从根节点开始，也不需要在叶子节点结束 
    # 所以必须要全部走一遍
    def preorder(self, root,sum):
        if not root: return
        self.countsum(root,sum)
        self.preorder(root.left, sum)
        self.preorder(root.right, sum)
        return

    # 计算每一个值 
    def countsum(self,root,sum):
        if not root: return
        if sum - root.val == 0: 
            self.count += 1
            # 因为可能会有0的出现 所以不能return
            # return self.count
        self.countsum(root.left, sum - root.val)
        self.countsum(root.right, sum - root.val)
        return self.count

    # 不需要从根节点开始，也不需要在叶子节点结束
    def FindPath(self , root: TreeNode, sum: int) -> int:
        # write code here
        if not root:
            return 0
        self.preorder(root, sum)
        return self.count