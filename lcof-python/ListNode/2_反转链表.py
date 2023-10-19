class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @return ListNode类
#
class Solution:
    def ReverseList(self , head: ListNode) -> ListNode:

        # 当head为空的时候 条件为true
        if not head:
            return None
        # pre = head 会断链
        # after = head.next
        after = head
        pre = None
        # after的next为None说明到了最后一个可以停止
        # 如果是pre则还会进行一次
        while after:
            temp = after.next
            after.next = pre
            pre = after
            after = temp
        # after此时为None
        return pre
    
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