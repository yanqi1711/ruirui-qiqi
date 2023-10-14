class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param lists ListNode类一维数组 
# @return ListNode类
#
class Solution:
    # 归并排序的分治
    def mergeKLists(self , lists: List[ListNode]) -> ListNode:
        # write code here
        if len(lists) <= 1:
            if len(lists) == 1:
                return lists[0]
            else:
                return None
        iMid = len(lists) // 2
        # 分治
        ListsLeft = self.mergeKLists(lists[:iMid])
        ListsRight = self.mergeKLists(lists[iMid:])
        # 左右两边是否为空
        if not ListsLeft:
            return ListsRight
        if not ListsRight:
            return ListsLeft
        # 获取头节点
        if ListsLeft.val <= ListsRight.val:
            temp = ListsLeft
            ListsLeft = ListsLeft.next
        else:
            temp = ListsRight
            ListsRight = ListsRight.next
        head = temp

        while ListsLeft and ListsRight:
            if ListsLeft.val <= ListsRight.val:
                temp.next = ListsLeft
                ListsLeft = ListsLeft.next
            else:
                temp.next = ListsRight
                ListsRight = ListsRight.next
            temp = temp.next

        if ListsLeft:
            temp.next = ListsLeft
        else:
            temp.next = ListsRight
        
        return head