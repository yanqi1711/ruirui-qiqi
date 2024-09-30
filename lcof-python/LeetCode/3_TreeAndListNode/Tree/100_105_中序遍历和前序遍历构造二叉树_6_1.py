# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        # 利用字典存储中序结果 因为前序遍历结点第一个就是当前子树的根节点
        # 通过值获取根节点在中序遍历中所在位置 这样就可以把inorder切分
        self.getInorderIndex = {ele:i for i,ele in enumerate(inorder)}
        def __BuildTree__(pre_left, pre_right, in_left, in_right):
            # 【】
            if pre_left > pre_right:
                return None
            # 前序遍历的第一个根结点的index
            pre_root_index = pre_left
            # 中序根节点的位置-->index
            in_root_index = self.getInorderIndex[preorder[pre_root_index]]
            
            # 建立根节点
            root = TreeNode(preorder[pre_root_index])
            # 左子树的节点 例: 0-0 没有左子树 1 - 0 即 左边有一个
            size_left_subTree = in_root_index - in_left
            # 连接左节点
            # 如果左子树为None 就是传入1,0 直接对应返回条件 传入None 有一个的时候 1,1->(中序遍历结果1-0)
            # 减去第一个根节点,划分左子树 不需要+1,左子树最左边,减去找到的root例子:1-1->获得左子树唯一一个节点
            root.left = __BuildTree__(pre_left+1, pre_left+size_left_subTree,in_left,in_root_index-1)
            # 连接右节点,
            root.right = __BuildTree__(pre_left+size_left_subTree+1,pre_right,in_root_index+1, in_right)
            return root
        return __BuildTree__(0,n-1,0,n-1)