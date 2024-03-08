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
# @param o1 int整型 
# @param o2 int整型 
# @return int整型
#
class Solution:
    def DFS(self, root, node:int, path: list):
        if not root:
            return
        path.append(root.val)
        # 相等直接结束
        if path[-1] == node: return
        #  完全不需要 判断是不是叶子结点 并且叶子结点是否等于node
        # if not root.left and not root.right and root.val != node:
        #     path.pop()
        #     return
        # 不相等接着遍历
        self.DFS(root.left, node, path)
        self.DFS(root.right, node, path)
        # 当前结点不等于node 其儿子结点也不等于就pop
        # 有一个等于就进入上一层循环了
        if path[-1] != node: 
            path.pop() 
            return


    def lowestCommonAncestor(self , root: TreeNode, o1: int, o2: int) -> int:
        # write code here
        p_path, q_path = [],[]
        self.DFS(root, o1, p_path)
        self.DFS(root, o2, q_path)
        print(p_path)
        print(q_path)
        # 遍历2个路径表 不要用for 容易越界
        i = 0
        while i < len(q_path) and i < len(p_path):
            if p_path[i] == q_path[i]:
                res = p_path[i]
                i += 1
            else:
                break
        return res