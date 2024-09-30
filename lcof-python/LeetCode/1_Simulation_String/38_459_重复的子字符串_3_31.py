""" # 超过5%的人
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        ans = ""
        m = len(s)
        for i in s:
            ans += i
            if ans == s:
                return False
            temp = ans
            while True:
                if temp == s:
                    return True
                n = len(temp)
                if n <= m:
                    temp+=ans
                else:
                    break 
        return False
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 移动匹配 前一段一定等于后一段（不一定对半）例: ababab ->abab ab == ab abab
        # 不等于才为True 等于说明到了第一个字符串的末尾
        return (s + s).find(s, 1) != len(s)
    
if __name__ == "__main__":
    s = Solution()
    print(s.repeatedSubstringPattern("aba"))