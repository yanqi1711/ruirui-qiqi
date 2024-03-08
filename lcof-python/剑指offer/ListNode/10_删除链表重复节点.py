class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pHead ListNode类 
# @return ListNode类
#
# 直接删除 省空间 一次遍历省时间
# class Solution:
#     def deleteDuplication(self , pHead: ListNode) -> ListNode:
#         #空链表
#         if pHead == None: 
#             return None
#         res = ListNode(0)
#         #在链表前加一个表头
#         res.next = pHead 
#         cur = res
#         while cur.next and cur.next.next: 
#             #遇到相邻两个节点值相同
#             if cur.next.val == cur.next.next.val: 
#                 temp = cur.next.val
#                 #将所有相同的都跳过
#                 while cur.next != None and cur.next.val == temp: 
#                     cur.next = cur.next.next
#             else:
#                 cur = cur.next
#         #返回时去掉表头
#         return res.next
class Solution:
    def deleteDuplication(self , pHead: ListNode) -> ListNode:
        # write code here
        if not pHead:
            return None
        hash_table = dict()
        cur = pHead
        while cur:
            if cur.val in hash_table.keys():
                hash_table[cur.val] = True
            else:
                hash_table[cur.val] = False
            cur = cur.next
        cur = pHead
        pre = None
        while cur:
            if hash_table[cur.val] == True:
                cur = cur.next
                if pre is not None:
                    pre.next = cur
                else:
                    # pre为空只能是第一个元素重复 所以pHead = pre == None
                    pHead = pre
            else:
                # 此时 哈希表情况为False 所以不是重复节点 需要重置表头
                # 防止 1 1 1 1 1 1 7情况
                if pre is None:
                    pre = cur
                    cur = cur.next
                    pHead = pre
                # 普通的连表情况
                else:
                    pre = cur 
                    cur = cur.next
        return pHead