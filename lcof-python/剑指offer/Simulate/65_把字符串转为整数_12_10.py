class Solution:
    def StrToInt(self , s: str) -> int:
        # 删去空格
        s = s.strip()
        # 判断是否为空
        if not s:
            return 0
        # 判断符号
        sign = -1 if s[0] == '-' else 1
        # 截取数字
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        # 结果
        num = 0
        # 遍历
        for i in s:
            # 是数字 *10 再相加
            if i.isdigit():
                num *= 10
                num += ord(i) - 48
            # 非数字直接跳出
            else:
                break
        return min(2 ** 31 -1, max(num * sign, - 2 ** 31))