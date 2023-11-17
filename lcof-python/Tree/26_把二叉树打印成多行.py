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
        if not pRoot:
            return []
        res = []
        q = queue.Queue()
        q.put(pRoot)
        while not q.empty():
            mylist = []
            new_queue = queue.Queue()
            while not q.empty():
                node = q.get()
                mylist.append(node.val)
                if node.left is not None:
                    new_queue.put(node.left)
                if node.right is not None:
                    new_queue.put(node.right)
            res.append(mylist)
            q = new_queue
        return res
