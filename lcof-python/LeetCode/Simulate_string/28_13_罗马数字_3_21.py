class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        n = len(s)
        for index in range(n-1):
            if d[s[index]] >= d[s[index+1]]:
                result += d[s[index]]
            else:
                result -=d[s[index]]
        result += d[s[-1]]
        return result