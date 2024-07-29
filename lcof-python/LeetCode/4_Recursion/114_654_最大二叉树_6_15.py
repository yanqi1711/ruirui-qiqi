# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        # 建立一个哈希存储值合idx的关系
        self.getIndex = {value:index for index,value in enumerate(nums)}
        def constructTree(left, right):
            if left > right:
                return None
            nonlocal nums
            cur = max(nums[left:right+1])
            curIndex = self.getIndex[cur]
            Node = TreeNode(cur)
            Node.left = constructTree(left, curIndex-1)
            Node.right = constructTree(curIndex+1, right)
            return Node
        return constructTree(0, len(nums)-1)