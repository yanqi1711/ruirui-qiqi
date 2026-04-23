# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # 一个没有用整数初始化的NestedInteger 就是一个[]
        # 加入数字需要先使用NestedInteger初始化 再用add加入进去
        # 只有一个数字
        if s[0] != '[':
            return NestedInteger(int(s))
        # stack 栈模拟 num计算数字 negative
        stack, num,negative= [], 0, 1
        for i, c in enumerate(s):
            if c == "-":
                negative = -1
            elif c == "[":
                stack.append(NestedInteger())
            elif c.isdigit():
                num = num *10 + int(c)
            elif c in ",]":
                    # 2种情况 前面是[31,[],222] 前面是']'
                    # 第二种数字结尾
                if s[i-1].isdigit():
                    stack[-1].add(NestedInteger(num * negative))
                # 进来了 就说明一个数或者[]结束了 需要重置
                num, negative = 0,1
                # 说明不是最开始的那个[] 是在内部嵌套的[]
                # 现在一个嵌套[]结束了,需要加入到上一个里
                if c == ']' and len(stack) > 1:
                    stack[-2].add(stack.pop())
        return stack.pop()