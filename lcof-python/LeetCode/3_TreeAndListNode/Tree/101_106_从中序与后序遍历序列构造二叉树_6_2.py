# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        idx_map = {ele:i for i,ele in enumerate(inorder)}
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            nonlocal postorder
            val = postorder.pop()
            root = TreeNode(val)
            # 
            index = idx_map[val]
            # 易错点 后序遍历 左右根 所以必须先右后左
            root.right = helper(index+1, in_right)
            root.left = helper(in_left, index-1)
            
            return root
        return helper(0, len(inorder)-1)