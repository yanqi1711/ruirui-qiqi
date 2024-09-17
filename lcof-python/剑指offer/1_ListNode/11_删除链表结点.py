class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @param val int整型 
# @return ListNode类
#
class Solution:
    def deleteNode(self , head: ListNode, val: int) -> ListNode:
        # write code here
        if not head:
            return None
        cur = head
        pre = ListNode(0)
        head = pre
        while cur:
            if cur.val == val:
                pre.next = cur.next
                break
            else:
                pre.next = cur
                pre = pre.next
                cur = cur.next
        return head.next