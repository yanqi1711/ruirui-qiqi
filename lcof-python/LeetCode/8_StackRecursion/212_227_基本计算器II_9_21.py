class Solution:
    def calculate(self, s: str) -> int:
        ans = []
        temp = []
        flag = 1
        mul,sub=False, False
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i+=1
                continue
            if s[i].isdigit():
                current_number = 0
                while i < len(s) and s[i].isdigit():
                    current_number = current_number * 10 + int(s[i])
                    i += 1
                ans.append(current_number * flag)
                flag = 1 #需要重置flag
                if temp:
                    if mul:
                        ans.append(temp.pop() * ans.pop())
                        mul = False
                    elif sub: #必须if 因为是 else不管如何上面的只要mul是False就一定走这里
                        # 不能整除
                        ans.append(int(temp.pop() / ans.pop()))
                        sub = False
                continue
            # 24_10_21不是用i检查
            if s[i] == "+":
                flag = 1
            elif s[i] == '-':
                flag = -1
            elif s[i] == '/':
                sub = True
                temp.append(ans.pop())
            elif s[i] == '*':
                mul = True
                temp.append(ans.pop())
            i+=1
        print(ans)
        return sum(ans)