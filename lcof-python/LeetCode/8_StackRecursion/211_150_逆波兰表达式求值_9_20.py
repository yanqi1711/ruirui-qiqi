class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = []
        for i in tokens:
            # isdigit()不支持负数
            if i.lstrip('-').isdigit():
                ans.append(i)
                continue
            # 先弹出两个操作数，注意顺序 直接pop除法会出错
            right = int(ans.pop())
            left = int(ans.pop())
            if i == "+":
                ans.append(left + right)
            elif i == '-':
                ans.append(left - right)
            elif i == '/':
                ans.append(int(left / right))  # 注意：Python 3 的 / 是浮点除法，需要转为整除
            elif i == '*':
                ans.append(left * right)
        return int(ans[-1])