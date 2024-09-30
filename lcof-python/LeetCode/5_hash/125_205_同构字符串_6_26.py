class Solution:
    # 和209一样
    def isIsomorphic(self, s: str, t: str) -> bool:
        #  return len(set(s))==len(set(t))==len(set(zip(s,t)))
        if len(s) != len(t):
            return False
        Dict = {}
        for i in range(len(s)):
            if s[i] in Dict:
                if Dict[s[i]] != t[i]:
                    return False
            else:
                # 判断
                if t[i] in Dict.values():
                    return False
                Dict[s[i]] = t[i]
        return True