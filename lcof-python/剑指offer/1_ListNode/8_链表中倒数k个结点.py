class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pHead ListNode类 
# @param k int整型 
# @return ListNode类
#
class Solution:
    def FindKthToTail(self , pHead: ListNode, k: int) -> ListNode:
        # write code here
        if not pHead:
            return None
        slow = pHead
        fast = pHead
        # k=1 fast.next == None
        while k:
            print(k)
            if fast != None:
                fast = fast.next
            else:
                return None
            k -= 1
        while fast:    
            slow = slow.next
            fast = fast.next
        return slow