class Solution:
    def isNumeric(self , str:str ):
        # write code here
        if not str:
            return False
        s = str.strip()
        if not s:
            return False
        length = len(s)
        # 四种状态
        is_dot = False
        is_num = False
        is_e_or_E = False
        # 逆向思维 满足那些状况返回False
        for i in range(length):
            # 有数字是正常的 设置为True
            if s[i] >= '0' and s[i] <= '9':
                is_num = True
            elif s[i] == '.':
                # 无重复小数点 无e
                # .123 可以转化为 0.123 是合法的
                # "123e1.12" 是非法的
                if is_dot or is_e_or_E:
                    return False
                is_dot = True
            elif s[i] == 'e' or s[i] == 'E':
                # 前面没有数字 前面有e
                if not is_num or is_e_or_E:
                    return False
                is_e_or_E = True
                # 重置数字 123e+ 遇到e后后面必须还要有数字
                is_num = False
            elif s[i] == '+' or s[i] == '-':
                # 符号不满足 第一个 and 只出现在e的后面 返回false
                if i != 0 and s[i-1] !='e' and s[i-1] != 'E':
                    return False
            else: # 遇到不是 数字 点 e/E +/- 直接返回False
                return False
        return is_num