class Solution:
    # 比438简单 是一个题
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len = len(s1),len(s2)

        if s2_len < s1_len:
            return False

        # 记录当前滑动窗口，如果在当前窗口就减少 如果移动了 那就需要把之前减少的给补到 0 
        count = [0] * 26
        # 记录p里面的词的数目
        for i in range(s1_len):
            count[ord(s1[i]) - 97]+=1
        # 因为至少有一个
        left = 0
        for right in range(s2_len):
            # 至少有一个 开始滑动
            count[ord(s2[right])-97] -=1
            # 1 当前窗口里面存在不是p里面的词语 s:cab  p:ab 所以需要移动窗口给他加上
            # 2 s: abcab p:ab 到c了 直接把left拉到c 因为之前ab被减少了 所以需要补起来
            # 3 s: abcde p:z  小于1直接把c 拉满
            while count[ord(s2[right]) - 97] < 0:
                # 补充到原始状态
                count[ord(s2[left]) - 97] += 1
                left += 1
            if right-left+1 == s1_len:
                return True
        return False