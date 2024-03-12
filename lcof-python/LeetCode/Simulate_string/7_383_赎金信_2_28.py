"""
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
如果可以，返回 true ；否则返回 false 。
magazine 中的每个字符只能在 ransomNote 中使用一次。
***
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        my_hash = {}
        index = 0
        for i in magazine:
            if i in my_hash.keys():
                my_hash[i] += 1
            else:
                my_hash[i] = 1
        for j in ransomNote:
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