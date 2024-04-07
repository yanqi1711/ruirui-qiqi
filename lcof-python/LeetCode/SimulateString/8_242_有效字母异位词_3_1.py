"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
"""
# 解法和赎金信一样
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_hash = {}
        index = 0
        for i in t:
            if i in my_hash.keys():
                my_hash[i] += 1
            else:
                my_hash[i] = 1
        for j in s:
            if j not in my_hash.keys():
                return False
            elif j in my_hash.keys():
                if my_hash[j] == 0:
                    return False
                else:
                    my_hash[j] -= 1
            else:
                continue
        return True