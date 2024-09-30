# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        #  1 1 1 1 1
        #            1 1 1 1
        #          1
        # A +B = B + A
        # 假设A先走完 A从头开始 等B到了结尾,A就走了m-n个位置 此时把B放回原点 两个一起走就可以碰到了
        A = headA
        B = headB
        while A != B:
            # 短的那个(跑的快的要到那个长的那里去 所以下面的else后面要是反的)
            A = A.next if A else headB
            B = B.next if B else headA
        return A