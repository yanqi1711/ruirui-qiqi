#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pushV int整型一维数组
# @param popV int整型一维数组
# @return bool布尔型
#
class Solution:
    def IsPopOrder(self, pushV: List[int], popV: List[int]) -> bool:
        # write code here
        if not pushV:
            return False
        if len(pushV) < len(popV):
            return False
        # n = len(pushV)
        # # 辅助栈
        # s = []
        # # 遍历入栈的下标
        # j = 0
        # # 遍历出栈的数组
        # for i in range(n):
        #     # 入栈：栈为空或者栈顶不等于出栈数组
        #     # j 只会增加 j=5 时就只有比较了
        #     while j < n and (len(s) == 0 or s[-1] != popV[i]):
        #         s.append(pushV[j])
        #         j += 1
        #     # 栈顶等于出栈数组
        #     if s[-1] == popV[i]:
        #         s.pop()
        #     # 不匹配序列
        #     else:
        #         return False
        # return True
        # 原地栈
        n = 0
        j = 0
        for i in pushV:
            pushV[n] = i
            # pushv有值的时候
            while n >= 0 and pushV[n] == popV[j]:
                j+=1
                n-=1

            n+=1
        # n 为当前计数 最后为0 表示两个完美匹配
        return True if n == 0 else False