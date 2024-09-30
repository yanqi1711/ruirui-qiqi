"""
给定一个字符串 s，统计并返回具有相同数量 0 和 1 的非空（连续）子字符串的数量，并且这些子字符串中的所有 0 和所有 1 都是成组连续的。

重复出现（不同位置）的子串也要统计它们出现的次数。
"""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        counts = []
        num0 = 0
        num1 = 0
        for i in s:
            if i == "0":
                num0 += 1
                if num1 != 0:
                    counts.append(num1)
                    num1 = 0
            else:
                num1 += 1
                if num0 != 0:
                    counts.append(num0)
                    num0 = 0
        counts.append(num0 or num1)
        sum = 0
        for j in range(len(counts) - 1):
            sum += min(counts[j],counts[j+1])
        return sum
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pre, cur, count, ppp = 0,1,0,s[0]
        # 动态规划
        for i in s[1:]:
            # 01转换 更新前面连续的数值pre cur设置为1
            if i != ppp:
                pre, cur = cur, 1
            else:
                cur+=1
            # 当前连续数量小于前面就加1 
            if cur<=pre:
                count+=1
            ppp = i
            
        return count