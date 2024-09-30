class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 如果分数能整除
        if numerator % denominator == 0:
            return str(numerator // denominator)

        # 符号判断
        s = []
        if (numerator < 0) ^ (denominator < 0):
            s.append('-')
        
        # 取绝对值
        numerator = abs(numerator)
        denominator = abs(denominator)

        # 整数部分
        integer = numerator // denominator
        s.append(str(integer))  # 使用 list 的 append 来构建字符串
        s.append('.')

        # 小数部分
        indexMap = {}
        remain = numerator % denominator
        
        # 在小数部分查找循环
        while remain and remain not in indexMap:
            indexMap[remain] = len(s)
            remain *= 10
            s.append(str(remain // denominator))  # 使用 append 来构建字符串
            remain %= denominator

        if remain:  # 说明找到了循环节
            index = indexMap[remain]
            s.insert(index, '(')  # 插入 '('
            s.append(')')  # 添加 ')'
        
        return ''.join(s)  # 使用 join 方法将 list 转为字符串
