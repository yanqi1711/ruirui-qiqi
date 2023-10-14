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
    def ReverseList(self , head: ListNode) -> ListNode:
        if head is None:
            return ListNode(None)
        a = head.next
        head.next = None
        
        
        return 
    
if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    l1.next = l2   
    l3 = ListNode(3)    
    l2.next = l3
    l4 = ListNode(4)
    l3.next = l4
    print(s.ReverseList(l1))