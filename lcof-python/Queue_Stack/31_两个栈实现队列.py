# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        # 讲结点push进去
        self.stack1.append(node)
    def pop(self):
        # return xx
        if self.stack2 == []:
            # 如股票stack1有数 全部push入stack2 然后stack2第一个就是
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()