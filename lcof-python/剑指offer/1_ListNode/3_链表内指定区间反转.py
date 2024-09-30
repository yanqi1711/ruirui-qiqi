class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @param m int整型 
# @param n int整型 
# @return ListNode类
#
# 非剑指offer
class Solution:
    def reverseBetween(self , head: ListNode, m: int, n: int) -> ListNode:
        # write code here
        if not head:
            return None
        if m == n:
            return head
        count = 1
        temp1 = head
        pre = None
        after = head
        while head:
            # 保存断掉的节点
            # 1 连接 4； 4 -》 head_connect.next = first
            # 2 连接 5； 5 -》 end.next = tail_connect
            #
            if count == m:
                head_connect = pre
                end = after
            if count == n:
                tail_connect = after.next
                first = after
            # 可能会导致断链 after == head
            # 3 个元素 调整2次链接
            if count >= m and count <=n:
                temp = after.next
                after.next = pre
                pre = after
                after = temp
                head = after
            else:
                pre = after
                after = after.next
                head = head.next
            count += 1
        # m == 1 1 链接 5 
        # n == 5 2 链接 Null
        if m == 1:
            end.next = tail_connect
            temp1 = first
        # elif (count - 1) == n:
        #     head_connect.next = first
        #     end.next = None
        # elif m == 1 and (count - 1) == n:
        #     pass
        else:
            end.next = tail_connect
            head_connect.next = first
        return temp1