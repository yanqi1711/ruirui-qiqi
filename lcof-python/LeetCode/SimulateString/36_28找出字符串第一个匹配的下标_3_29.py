def build_next(patt):
    next = [0]
    prefix_len = 0
    # 第一个已经确定
    i = 1
    while i < len(patt):
        # 如果该前缀=后缀+1 如果一直想等一直+1 因为前面都是一样的最后都会跳到一个位置
        if patt[i] == patt[prefix_len]:
            prefix_len+=1
            next.append(prefix_len)
            i+=1
        else:
            # 没有相同前缀了
            if prefix_len == 0:
                next.append(0)
                i+=1
            else:
                # 前面有几个相同的前缀
                prefix_len = next[prefix_len-1]
    return next
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(haystack)
        lengthNext = len(needle)
        if lengthNext == 0:
            return 0
        next = build_next(needle)
        j = 0
        for i in range(length):
            while(j > 0 and haystack[i] != needle[j]):
                j = next[j-1]
            if haystack[i] == needle[j]:
                j+=1
            if (j==lengthNext):
                return i - lengthNext + 1
        return -1