import queue
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
# @return int整型二维数组
#
class Solution:
    def Print(self , pRoot: TreeNode) -> List[List[int]]:
        # write code here
        # 判断空树
        if not pRoot:
            return []
        head = pRoot
        res = []
        q = queue.Queue()
        flag = True
        q.put(head)
        # q为空返回True
        while not q.empty():
            row = []
            flag = not flag
            length = q.qsize()
            for i in range(length):
                temp = q.get()
                row.append(temp.val)
                if temp.left:
                    q.put(temp.left)
                if temp.right:
                    q.put(temp.right)
            # 偶数就反转
            if flag:
                row = row[::-1]
            res.append(row)
        return res