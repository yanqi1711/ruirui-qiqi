class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        word2char = {}
        char2word = {}
        # 双向检查
        for c, w in zip(pattern, words):
            # 检查 a->dog
            if c in char2word:
                if char2word[c] != w:
                    return False
            else:
                char2word[c] = w
            
            # 检查dog->a是否对应
            if w in word2char:
                if word2char[w] != c:
                    return False
            else:
                word2char[w] = c
        return True
    # 一个字典
    def wordPattern2(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        myDict = {}
        for i in range(len(pattern)):
            # 匹配
            if pattern[i] in myDict:
                if myDict[pattern[i]] != s[i]:
                    return False
            else: # 此时pattern[i]不在字典里
                # 先检查当前单词是否已经匹配 比如 a->dog b->dog 返回False
                if s[i] in myDict.values(): 
                    return False
                myDict[pattern[i]] = s[i]
        return True