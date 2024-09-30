"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(Node):
            # 记录头结点
            cur = Node
            # 记录尾结点
            last = None
            while cur:
                # 因为不知道child是否存在,先记录下一个结点情况
                next = cur.next
                if cur.child:
                    # 递归找到child结点最后的一个
                    # 因为是递归所以肯定能返回最后一结点 但是此时cur是没有变化的
                    lastChild = dfs(cur.child)
                    # 连接cur
                    cur.next = cur.child
                    cur.child.prev = cur
                    cur.child = None
                    # 如果cur.next不为空 把child的最后一个和cur.next连接
                    if next:
                        next.prev = lastChild
                        lastChild.next = next

                    last = lastChild
                else:
                    # 没有child 保证 last是有值的 因为要返回last不为空
                    last = cur
                # 直接更新到next 因为没有child直接cur.next 有child需要更新到child后面的next
                # 因为经过递归后中间一定没有了child
                cur = next
            return last
        dfs(head)
        return head
