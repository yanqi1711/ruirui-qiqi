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
# @param p int整型 
# @param q int整型 
# @return int整型
#
class Solution:
    # 二叉搜索树
    def get_path(self, root, target):
        path = []
        node = root
        while node.val != target:
            path.append(node.val)
            if node.val < target:
                node = node.right
            else:
                node = node.left
        # 保存找到的那一个
        path.append(node.val)
        return path
    def lowestCommonAncestor(self , root: TreeNode, p: int, q: int) -> int:
        # write code here
        p_path, q_path = self.get_path(root, p) ,self.get_path(root, q)
        # 遍历2个路径表 不要用for 容易越界
        i = 0
        while i < len(q_path) and i < len(p_path):
            if p_path[i] == q_path[i]:
                res = p_path[i]
                i += 1
            else:
                break
        return res