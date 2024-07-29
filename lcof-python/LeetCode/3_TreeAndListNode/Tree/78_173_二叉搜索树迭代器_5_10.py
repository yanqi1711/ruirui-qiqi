# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.cur = 0
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            self.stack.append(root.val)
            inOrder(root.right)
        inOrder(root)
        print(self.stack)
        return None

    def next(self) -> int:
        if self.cur < len(self.stack):
            result = self.stack[self.cur]
            self.cur += 1
            return result

    def hasNext(self) -> bool:
        if self.cur < len(self.stack):
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()