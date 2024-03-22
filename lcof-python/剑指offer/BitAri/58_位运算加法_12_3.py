class Solution:
    def Add(self , num1: int, num2: int) -> int:
        # 非进位和 n = a ^ b
        # 进位和   (c = a & b) << 1
        add = num2
        res = num1
        while add:
            # 第一步 求n 没有进位 这就是答案
            n = add ^ res
            # 第二步 求 add 可能进位与异或后数据相加 仍然有进位
            add = (add & res) << 1
            # python无限长度 需要截断
            res = n & 0xffffffff
        # 因为python无限长度 所以需要自己模拟补码 作用其实就是高位设置为1  高位置为1:即负数(按位取反)
        return res if res >> 31 == 0 else ~(res ^ 0xffffffff)