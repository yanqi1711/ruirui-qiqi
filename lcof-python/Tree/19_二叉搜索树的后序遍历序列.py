# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param sequence int整型一维数组 
# @return bool布尔型
#
# 还有辅助栈的方法法
class Solution:
    def VerifySquenceOfBST(self , sequence: List[int]) -> bool:
        # write code here
        # 递归 
        # 1:先找到root 然后第一个大于root的就是左右子树的分隔点 记录其index
        # 2:只需要判断右子树 index,length-1 是否都大于root，因为递归后最开始的左子树也会被划分
        # 重要--->3:递归结束条件 边界判断 index < 0 不需要递归 index > length-1 直接结束
        # 4:判断左右子树是否满足条件 --> 递归
        # 5:当left 和 right都为true即为返回条件
        if not sequence:
            return False
        length = len(sequence)
        root = sequence[-1]
        index = 0
        ###### 必须为length 防止右子树不存在  ######
        for i in range(length):
            # 只有左子树情况下 sequence[i] = root
            if sequence[i] >= root:
                index = i
                break
        for j in range(index, length-1):
            if sequence[j] < root:
                return False
        # 先验证左边
        left = True
        if index > 0:
            left = self.VerifySquenceOfBST(sequence[:index])
        right = True
        # 设置条件防止最后一个继续递归
        if index < length - 1:
            right = self.VerifySquenceOfBST(sequence[index:-1])
        return left and right