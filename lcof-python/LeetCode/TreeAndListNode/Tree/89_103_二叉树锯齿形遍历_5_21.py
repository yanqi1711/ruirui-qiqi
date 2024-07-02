# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        ans = [[root.val]]
        flag = True
        while q:
            flag = not flag
            curLayer = []
            nodeLayer = []
            while q:
                node = q.popleft()
                if node.left:
                    nodeLayer.append(node.left)
                    curLayer.append(node.left.val)
                if node.right:
                    nodeLayer.append(node.right)
                    curLayer.append(node.right.val)
            if flag == False:
                curLayer.reverse()
            ans.append(curLayer)
            q = deque(nodeLayer)
        return ans[:-1]