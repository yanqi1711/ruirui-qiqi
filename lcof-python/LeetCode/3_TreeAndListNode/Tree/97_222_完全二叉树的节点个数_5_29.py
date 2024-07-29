class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional


class Solution:
    # log^2(n)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        temp = root
        depth = 0
        while temp.left:
            depth += 1
            temp = temp.left
        # depth是最深的层 故left是他的最小值 right是最大值
        left,right = 1 << depth,(1<<(depth+1))-1
        while left < right:
            mid = (right - left +1) // 2 + left
            print(mid)
            if self.exists(root, depth, mid):
                left = mid
            else:
                right = mid -1
        return left

    def exists(self, node, depth:int, existValue:int):
        # 第depth层的数 第一位都是1 之后的位数从高到低表示了 它从根结点 到当前结点的路径故需要-1
        bits = 1 << (depth - 1)
        # 从高到低按位与运算 为0 向左 为1 向右 不为空就表示还有 
        # 如果大于0表示还没到当前层的最后一个 因为bits可以表示当前层的所有状态 比如第三层 bits = 10
        # 就代表2位数 00 01 10 11 四个树 根据每次与的结果不同获取根结点路径 所以bits = 0 代表全部遍历完成
        root = node
        while root != None and bits > 0:
            if bits & existValue:
                root = root.right
            else:
                root = root.left
            # 每次都要更新状态
            bits >>= 1
        # 如果存在 则是bits遍历完了 都还有 所以是 True 即找到了 
        # 不存在 就是root == None了 直接返回
        return root != None
    # 层序遍历 有一个为空直接跳出 计算结果即可 O(n)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 0
        q = deque([root])
        while q:
            leaveNode = []
            depth +=1
            while q:
                node = q.popleft()
                if node.left is None:
                    return 2 ** depth - 1 + len(leaveNode)
                leaveNode.append(node.left)   
                if node.right is None:
                    return 2 ** depth - 1 + len(leaveNode)
                leaveNode.append(node.right)
            q = deque(leaveNode)
        return 2 *depth -1