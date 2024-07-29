class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        length = 0
        for i in s:
            if i!="-":
                length+=1
        firstLen = length % k
        result = str()
        temp = k
        for j in s:
            if j != "-":
                if firstLen:
                    result += j.upper()
                    firstLen-=1
                    if firstLen == 0:
                        result += "-"
                elif temp:
                    result += j.upper()
                    temp -=1
                    if temp == 0:
                        result +="-"
                        temp = k
        if result and result[-1] == "-":
            result = result[:-1]
        return result
    
if __name__ == "__main__":
    s = Solution()
    print(s.licenseKeyFormatting("5F3Z-2e-9-w",4))