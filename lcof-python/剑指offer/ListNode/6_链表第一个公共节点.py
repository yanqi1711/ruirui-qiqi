# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param pHead1 ListNode类 
# @param pHead2 ListNode类 
# @return ListNode类
#
# 哈希实现
class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        # write code here
        # 需要额外空间
        if pHead1 is None or pHead2 is None:
            return None
        hash_table = set()
        head1 = pHead1
        head2 = pHead2
        while pHead1:
            hash_table.add(pHead1)
            pHead1 = pHead1.next
        
        while pHead2:
            if pHead2 in hash_table:
                return pHead2
            pHead2 = pHead2.next
        return None