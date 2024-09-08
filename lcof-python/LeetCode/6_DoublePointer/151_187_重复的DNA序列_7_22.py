class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10: return []
        ans = []
        sub = s[:10]
        d = {sub:1}
        for i in range(10,len(s)):
            sub+=s[i]
            sub = sub[1:]
            if sub in d:
                if d[sub] == 1:
                    ans.append(sub)
                    d[sub] += 1
                else:
                    continue
            else:
                d[sub] = 1
        return ans
                