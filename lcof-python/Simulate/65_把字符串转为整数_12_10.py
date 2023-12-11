class Solution:
    def StrToInt(self , s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        sign = -1 if s[0] == '-' else 1
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        num = 0
        for i in s:
            if i.isdigit():
                num *= 10
                num += ord(i) - 48
            else:
                break
        return min(2 ** 31 -1, max(num * sign, - 2 ** 31))