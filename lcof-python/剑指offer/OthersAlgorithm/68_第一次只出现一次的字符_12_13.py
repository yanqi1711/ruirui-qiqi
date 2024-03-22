class Solution:
    def FirstNotRepeatingChar(self , str: str) -> int:
        if len(str) == 1:
            return -1
        hash = dict()
        for i in str:
            if i in hash.keys():
                hash[i] += 1
            else:
                hash[i] = 1
        for key,value in hash.items():
            if value == 1:
                return str.index(key)
        return -1