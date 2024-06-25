# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 中序遍历
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getLength(head:ListNode):
            ret = 0
            while head:
                ret += 1
                head = head.next
            return ret
        def buildTree(left, right):
            # 左闭 右闭 所以left==right是合法区间
            if left > right:
                return None
            mid = (left+right)>>1
            # 中序遍历
            root = TreeNode()
            root.left = buildTree(left, mid-1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = buildTree(mid+1, right)
            return root
        length = getLength(head)
        return buildTree(0, length - 1)

# 快一些
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getMedian(left: ListNode, right: ListNode) -> ListNode:
            # 快慢指针 抓中位数 从left开始 少了很多不需要的操作
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def buildTree(left: ListNode, right: ListNode) -> TreeNode:
            if left == right:
                return None
            mid = getMedian(left, right)
            root = TreeNode(mid.val)
            root.left = buildTree(left, mid)
            root.right = buildTree(mid.next, right)
            return root
        
        return buildTree(head, None)
# class Solution:
#     def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
#         # 从头开始找 慢
#         def getRoot(mid:int):
#             if mid == 0:
#                 return head
#             cur = head
#             while mid:
#                 if cur.next:
#                     cur = cur.next
#                 mid -= 1
#             return cur
#         def helper(left,right):
#             if left>right:
#                 return None
#             mid = (left+right)>>1
#             root = getRoot(mid)
#             print(root.val)
#             root = TreeNode(root.val)
#             root.left = helper(left, mid-1)
#             root.right = helper(mid+1, right)
#             return root
#         temp = head
#         length = 0
#         while temp:
#             length+=1
#             temp = temp.next
#         return helper(0, length-1)
            
            