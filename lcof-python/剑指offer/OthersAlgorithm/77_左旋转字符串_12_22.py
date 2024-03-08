class Solution:
    def LeftRotateString(self , str: str, n: int) -> str:
        if not str:
            return ""
        if n == 0:
            return str
        length = len(str)
        while n > length:
            n = n % length
        str1,str2 = str[:n],str[n:]
        str = str2 + str1
        return str