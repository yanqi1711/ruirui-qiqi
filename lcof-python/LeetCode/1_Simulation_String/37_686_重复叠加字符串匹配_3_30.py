class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        m,n = len(a),len(b)
        maxCount = n // m
        result = 1
        temp = a
        print(maxCount)
        while result <= maxCount + 2:
            if b in a:
                return result
            a += temp
            result+=1
        return -1
    


if __name__ == "__main__":
    s = Solution()
    print(s.repeatedStringMatch("abc","cabcabca"))