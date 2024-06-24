# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate(start, end):
            # 如果start == end 那么就自身一个结点
            if start > end:
                return [None,]
            
            allList = []
            # 遍历所有情况
            for i in range(start, end+1):
                # i自身最后只需要把左边和右边所有情况拼起来返回
                # 找到当前i的左边所有结点情况 从start开始 到i-1结束
                left = generate(start,i-1)
                # 右边结点所有情况 
                right = generate(i+1, end)

                # 相当于不同二叉搜索树的 dp[i] +=dp[i-1]*dp[j-1]
                for l in left:
                    for r in right:
                        temp = TreeNode(i)
                        temp.left = l
                        temp.right = r
                        # 每一次匹配都是一种情况
                        allList.append(temp)
            return allList
        return generate(1,n) if n else []