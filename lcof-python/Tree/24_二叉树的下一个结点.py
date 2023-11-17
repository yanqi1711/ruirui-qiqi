# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    # 要先找到根节点 next指向父结点->找根结点的
    def __init__(self) -> None:
        self.list = []

    def inorder(self, pNode):
        if not pNode: return
        self.inorder(pNode.left)
        print(pNode.val)
        self.list.append(pNode)
        self.inorder(pNode.right)
        return

    def GetNext(self, pNode):
        # write code here
        root = pNode
        while root.next:
            root = root.next
        self.inorder(root)
        print(self.list)
        flag = False
        for i in self.list:
            if i == pNode:
                flag = True
                continue
            if flag == True:
                return i
        return None