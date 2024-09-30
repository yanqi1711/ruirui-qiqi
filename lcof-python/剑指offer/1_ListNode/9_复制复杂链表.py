# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return pHead
        cur = pHead
        # 创建新的链表节点，并且将其与原链表连接到一起 
        # 此时随机结点还没有new出来，不能连接
        # 此种方法需要遍历三次链表 第一次n 第二次第三次2n 时间复杂度为o(n)
        # 但是空间复杂度为o(n)
        while cur:
            clone = RandomListNode(cur.label)
            clone.next = cur.next
            cur.next = clone
            cur = clone.next
        # 连接随机结点
        # 初始化结点位置
        cur = pHead
        clone = cur.next
        res = cur.next
        while cur:
            # 末尾结点不能为空
            if cur.random == None:
                clone.random = None
                cur = clone.next
                if cur != None:
                    clone = cur.next
            else:
                # cur的next就是重新生成的结点
                clone.random = cur.random.next
                cur = clone.next
                if cur != None:
                    clone = cur.next
        #  开始断链
        cur = pHead
        clone = cur.next
        while cur:
            # cur.next 必定不为空
            cur.next = clone.next
            cur = cur.next
            # 判断cur是否为None -> 检查末尾
            if cur is not None:
                clone.next = cur.next
                clone = clone.next
        return res