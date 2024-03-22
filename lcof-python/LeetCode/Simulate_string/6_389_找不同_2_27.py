# 给定两个字符串 s 和 t ，它们只包含小写字母。
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
# 请找出在 t 中被添加的字母。
class Solution:
    # 136. 只出现一次的数字
    def findTheDifference(self, s: str, t: str) -> str:
        # 1 加ascii码
        sum = 0
        for i in s:
            sum += ord(i)
        for j in t:
            sum -= ord(j)
        return chr(-sum)
        