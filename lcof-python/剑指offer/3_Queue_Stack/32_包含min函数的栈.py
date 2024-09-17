# -*- coding:utf-8 -*-

class Solution:
   # 太慢
    # def __init__(self) -> None:
    #     self.min_node = None
    #     self.stack = []
    # def push(self, node):
    #     # write code here
    #     self.stack.append(node)
    #     if self.min_node == None:
    #         self.min_node = node
    #     if self.min_node > node:
    #         self.min_node = node

    # def pop(self):
    #     # write code here
    #     self.stack.pop()
    # def top(self):
    #     # write code here
    #     return self.stack[-1]
    # def min(self):
    #     # write code here
    #     self.min_node = min(self.stack)
    #     return self.min_node
    def __init__(self):
        self.stack = []

    def push(self, node):
        # write code here
        if not self.stack:
            self.stack.append((node, node))
        else:
            # 将当前最小值 保存了起来
            self.stack.append((node, min(node, self.stack[-1][1])))
    def pop(self):
        # write code here
        self.stack.pop()
    def top(self):
        # write code here
        return self.stack[-1][0]
    def min(self):
        # write code here
        return self.stack[-1][1]