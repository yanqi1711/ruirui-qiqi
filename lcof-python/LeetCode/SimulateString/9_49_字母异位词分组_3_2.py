"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hash2 = {}
        for j in strs:
            temp = sorted(j)
            temp = str(temp)
            if temp not in hash2.keys():
                hash2[temp] = ["".join(j)]
            else:
                hash2[temp].append("".join(j))
        for _,items in hash2.items():
            result.append(items)
        return result