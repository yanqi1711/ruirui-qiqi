# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Create a new node for each original node and store the mapping
        old_to_new = {}
        cur = head
        # 创建新的结点
        while cur:
            copy = Node(cur.val)
            # 把旧结点和新结点形成映射
            old_to_new[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            # 获取新的结点
            copy = old_to_new[cur]
            # 如果有next 直接就映射到 next 的结点
            copy.next =  old_to_new.get(cur.next)
            # get获取random 没有就是None
            copy.random = old_to_new.get(cur.random)
            cur = cur.next
        return old_to_new[head]