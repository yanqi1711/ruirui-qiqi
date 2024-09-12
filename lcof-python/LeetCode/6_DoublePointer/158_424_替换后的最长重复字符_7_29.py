class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0]*26
        left,right = 0,0
        # 记录出现最多字符数量 因为这样就要k这个数值来补
        curMax = 0
        while right < len(s):
            count[ord(s[right]) - 65] += 1
            # 记录出现最多的词
            curMax = max(curMax, count[ord(s[right]) - 65])
            # 如果没有过这里 其实滑动窗口一直在扩大也就是保持最大值 
            # 扩到最大值后就会一直保持 因为每次都是+1 -1
            if right - left + 1 - curMax > k:
                # 这里滑动左窗口
                count[ord(s[left]) - 65] -= 1
                left += 1
            right += 1
        # 因为循环跳出时 right 直接+1了
        return right - left