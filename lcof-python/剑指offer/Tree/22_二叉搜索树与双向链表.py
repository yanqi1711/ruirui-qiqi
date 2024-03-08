class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
# 
# @param pRootOfTree TreeNode类 
# @return TreeNode类
# 可以使用数组将中序遍历结点保存起来 然后再连接 不过需要开辟数组
# 递归调用栈
class Solution:
    def __init__(self) -> None:
        self.pre = None
        self.root = None

    def Convert(self , pRootOfTree ):
        # write code here
        if not pRootOfTree: return

        self.Convert(pRootOfTree.left)
        if self.root == None:
            self.root = pRootOfTree
        # 前一个结点不为空
        if self.pre != None:
            self.pre.right = pRootOfTree
            pRootOfTree.left = self.pre

        self.pre = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.root