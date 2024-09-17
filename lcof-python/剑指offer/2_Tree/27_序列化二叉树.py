# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self) -> None:
        # 序列化
        self.str = []
        # 反序列化
        self.start = -1

    def Serialize(self, root):
        # write code here
        if not root:
            self.str.append('#')
            return self.str
        self.str.append(root.val)
        self.Serialize(root.left)
        self.Serialize(root.right)
        return self.str

    def Deserialize(self, s):
        # write code here
        self.start += 1
        if s[self.start] == '#' or self.start > len(s) or not s:
            return
        node = TreeNode(int(s[self.start]))
        node.left = self.Deserialize(s)
        node.right = self.Deserialize(s)

        return node