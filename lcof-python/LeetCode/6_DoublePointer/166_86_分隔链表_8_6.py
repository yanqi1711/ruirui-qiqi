# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        # target.next是返回值
        target = slow = ListNode(0, head)
        pre_fast = None
        fast = head
        while fast:
            # 前面一起走 第一次slow.next是fast 直到找到第一个大于x的值
            while fast and slow.next.val < x:
                slow = slow.next
                pre_fast = fast
                fast = fast.next
            # fast找到小于x的值 就要开始插入了
            # fast首先要存在 
            while fast and fast.val >=x :
                pre_fast = fast
                fast = fast.next
            if fast: # 不存在直接跳出
                # 开始更新
                pre_fast.next = fast.next
                fast.next = slow.next
                slow.next = fast
                # 更新slow fast
                slow = slow.next
                fast = pre_fast.next
        return target.next
                