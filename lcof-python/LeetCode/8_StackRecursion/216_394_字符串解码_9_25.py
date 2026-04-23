class Solution:
    def decodeString(self, s: str) -> str:
        # 初始化两个栈，一个存数字，一个存字符串
        num_stack = []
        str_stack = []
        
        ans = ''  # 当前解析的字符串
        num = 0   # 当前解析的数字
        
        # 遍历字符串
        for char in s:
            if char.isdigit():  # 如果当前字符是数字，计算当前数字
                num = num * 10 + int(char)
                
            elif char == '[':  # 遇到左括号，把数字和当前字符串压入栈
                num_stack.append(num)  # 存数字
                str_stack.append(ans)  # 存当前字符串
                ans = ''  # 清空当前字符串
                num = 0   # 清空当前数字
                
            elif char == ']':  # 遇到右括号，弹出栈顶数字并重复字符串
                repeat_times = num_stack.pop()  # 取出数字
                last_str = str_stack.pop()  # 取出栈顶的字符串
                ans = last_str + ans * repeat_times  # 将当前字符串重复指定次数并与之前的字符串拼接
            else:  # 普通字符，直接拼接到当前字符串
                ans += char
        return ans
