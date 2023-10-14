# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param listNode ListNode类 
# @return int整型一维数组
# -> List[int]
class Solution:
    def printListFromTailToHead(self , listNode: ListNode):
        if listNode is None:
            return []
        a = []
        try:
            while True:
                a.append(listNode.val)
                listNode = listNode.next
        except:
            pass
        return a[::-1]
    
if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    l1.next = l2   
    l3 = ListNode(3)    
    l2.next = l3
    l4 = ListNode(4)
    l3.next = l4
    print(s.printListFromTailToHead(l1))