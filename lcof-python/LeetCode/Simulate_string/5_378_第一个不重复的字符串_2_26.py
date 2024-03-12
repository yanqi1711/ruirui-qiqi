class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        my_hash = {}
        for i in range(len(s)):
            if s[i] not in my_hash.keys():
                my_hash[s[i]] = [i,1]
            else:
                my_hash[s[i]][1] += 1
        for _,value in my_hash.items():
            if value[1] == 1:
                return value[0]
            else:
                continue
        return -1