class Solution:
    # 较慢
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        cmp = ''
        cnt = 0
        for i in range(len(s)):
            if s[i] in cmp:
                cnt = max(cnt, len(cmp))
                cmp = cmp[cmp.index(s[i])+1:]
            cmp+=s[i]
        return max(cnt, len(cmp))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = -1
        maximum = 0
        d = {}
        
        for i in range(len(s)):
            # 如果存在 设置新的开始结点不需要真的删除 只需要更新start 覆盖就行
            if s[i] in d and d[s[i]] > start:
                # 滑动窗口开始
                start = d[s[i]]
                # 覆盖旧的
                d[s[i]] = i
            else:
                # 增加新的
                d[s[i]] = i
                # 记录最大值
                if i - start > maximum:
                    maximum = i - start
        
        return maximum