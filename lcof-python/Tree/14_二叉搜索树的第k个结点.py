class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param proot TreeNode类 
# @param k int整型 
# @return int整型
#

class Solution:
    @staticmethod
    def KthNode_stack(proot:TreeNode,k:int):
        if not proot:
            return -1
        count = 0
        p = []
        while (len(p) != 0) or proot is not None:
            while proot:
                p.append(proot)
                proot = proot.left
            temp = p[-1]
            p.pop()
            count += 1
            if count == k:
                return temp.val
            proot = temp.right
        return -1

    def __init__(self) -> None:
        self.res = None
        self.count = 0

    def middleOrder(self, root, k):
        if not root or self.count > k:
            return
        # 先向左 最左边先计数
        self.middleOrder(root.left,k)
        self.count += 1
        if self.count == k:
            self.res = root
        self.middleOrder(root.right,k)

    def KthNode(self , proot: TreeNode, k: int) -> int:
        # write code here
        self.middleOrder(proot,k)
        if self.res:
            return self.res.val
        else:
            return -1