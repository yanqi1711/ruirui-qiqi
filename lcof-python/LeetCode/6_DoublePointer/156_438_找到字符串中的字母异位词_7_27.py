from typing import List


class Solution:
    # 一个集合
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s),len(p)

        if s_len < p_len:
            return []
        
        ans = []
        # 记录当前滑动窗口，如果在当前窗口就减少 如果移动了 那就需要把之前减少的给补到 0 
        count = [0] * 26
        # 记录p里面的词的数目
        for i in range(p_len):
            count[ord(p[i]) - 97]+=1
        # 因为至少有一个
        left = 0
        for right in range(s_len):
            # 至少有一个 开始滑动
            count[ord(s[right])-97] -=1
            # 1 当前窗口里面存在不是p里面的词语 s:cab  p:ab 所以需要移动窗口给他加上
            # 2 s: abcab p:ab 到c了 直接把left拉到c 因为之前ab被减少了 所以需要补起来
            # 3 s: abcde p:z  小于1直接把c 拉满
            while count[ord(s[right]) - 97] < 0:
                # 补充到原始状态
                count[ord(s[left]) - 97] += 1
                left += 1
            if right-left+1 == p_len:
                ans.append(left)
        return ans 
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s),len(p)

        if s_len < p_len:
            return []
        
        ans = []
        # 记录当前滑动窗口
        s_count = [0] * 26
        p_count = [0] * 26

        for i in range(p_len):
            # ord ->char转ascii码
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1
        
        if s_count == p_count:
            ans.append(0)
        
        for i in range(s_len-p_len):
            # 第一个已经比较过了 直接进入第二个
            # 所以需要先减 后增
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1
            
            if s_count == p_count:
                ans.append(i + 1)

        return ans