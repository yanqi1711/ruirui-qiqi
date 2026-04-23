# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # 每个元素要么是一个整数，要么是一个列表
        self.ans = []
        def dfs(NestedNode:NestedInteger):
            if NestedNode.isInteger():
                self.ans.append(NestedNode.getInteger())
            else:
                for i in NestedNode.getList():
                    dfs(i)
        for i in nestedList:
            dfs(i)
        self.index = -1
    def next(self) -> int:
        self.index += 1
        return self.ans[self.index]
        
    
    def hasNext(self) -> bool:
        return self.index + 1 < len(self.ans)
         