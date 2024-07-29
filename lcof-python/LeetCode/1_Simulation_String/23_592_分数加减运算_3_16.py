"""
给定一个表示分数加减运算的字符串 expression ，你需要返回一个字符串形式的计算结果。 

这个结果应该是不可约分的分数，即最简分数。 如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1。所以在上述例子中, 2 应该被转换为 2/1。
示例 1:

输入: expression = "-1/2+1/2"
输出: "0/1"
 示例 2:

输入: expression = "-1/2+1/2+1/3"
输出: "1/3"
示例 3:

输入: expression = "1/3-1/2"
输出: "-1/6"
"""
class Solution:
    def fractionAddition(self, expression: str) -> str:
        x,y = 0,1
        m= 0
        length = len(expression)
        i = 0
        while i < length:
            sign = 1
            x1 = 0
            if expression[i] == "-" or expression[i] == "+":
                if expression[i] == "-":
                    sign = -1
                i+=1
            while i < length and expression[i].isdigit():
                x1 = x1*10 + int(expression[i])
                i+=1
            x1 = sign * x1
            i +=1
            y1 = 0
            while i<length and expression[i].isdigit():
                y1 = y1*10 + int(expression[i])
                i += 1
            x = x * y1 + y * x1
            y = y1 * y
        if x == 0:
            return "0/1"
        g = gcd(abs(x), y)
        return f"{x // g}/{y // g}"