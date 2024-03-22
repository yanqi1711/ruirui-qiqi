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
# @param target int整型
# @return int整型二维数组
#
class Solution:
    def FindPath(self, root: TreeNode, target: int) -> List[List[int]]:
        # write code here
        res, path = [], []
        def dfs(root, target):
            # 处理空
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right and target - root.val == 0:
                # 要的是链表不是地址
                res.append(path[:])
            dfs(root.left, target - root.val)
            dfs(root.right, target - root.val)
            path.pop()
        dfs(root,target)
        return res