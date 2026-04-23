"""
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
'+' 不能用作一元运算(例如， "+1" 和 "+(2 + 3)" 无效)
'-' 可以用作一元运算(即 "-1" 和 "-(2 + 3)" 是有效的)
输入中不存在两个连续的操作符
每个数字和运行的计算将适合于一个有符号的 32位 整数
"""
class Solution:
    def calculate(self, s: str) -> int:
        opeator = [1]
        sign = 1
        i = 0
        ans = 0
        while i < (n:=len(s)):
            if s[i] == " ":
                i+=1
            elif s[i] == "+":
                # 得到正负
                sign = opeator[-1]
                i+=1
            elif s[i]== "-":
                sign = -opeator[-1]
                i+=1
            elif s[i] == '(':
                # 将之前的正负情况进入 本质是记录前面的正负 直接解开括号的流程
                opeator.append(sign)
                i+=1
            elif s[i] == ")":
                # 将记录的符号弹出
                opeator.pop()
                i+=1
            else:
                # 到数字结果了
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord('0')
                    i+=1
                # 需要记录符号
                ans += num * sign
        return ans