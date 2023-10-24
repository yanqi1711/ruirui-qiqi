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
# @param root TreeNode类 
# @return int整型一维数组
#
class Solution:
    def PrintFromTopToBottom(self , root: TreeNode) -> List[int]:
        # write code here
        if not root:
            return []
        my_res = []
        my_queue = queue.Queue()
        my_queue.put(root)
        while not my_queue.empty():
            Node = my_queue.get()
            my_res.append(Node.val)
            if Node.left:
                my_queue.put(Node.left)
            if Node.right:
                my_queue.put(Node.right)
        return my_res