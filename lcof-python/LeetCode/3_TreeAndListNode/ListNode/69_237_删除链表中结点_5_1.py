# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 解法1 一个一个移动 类似vector
        while node.next.next:
            node.val = node.next.val
            node = node.next
        node.val = node.next.val
        node.next = None
        # 2 直接把后面一个的val拿过来 然后删掉就可以了
        node.val = node.next.val
        node.next = node.next.next
