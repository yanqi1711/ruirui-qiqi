"""
给定一个字符串 s ，根据字符出现的 频率 对其进行 降序排序 。一个字符出现的 频率 是它出现在字符串中的次数。
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        hash = {}
        for i in s:
            if i in hash.keys():
                hash[i] += 1
            else:
                hash[i] = 1
        result = []
        sorted_items = sorted(hash.items(),key = lambda x:x[1],reverse = True)
        print(sorted_items)
        for key, value in sorted_items:
            while(value):
                value -=1
                result.append(key)
        return "".join(result)