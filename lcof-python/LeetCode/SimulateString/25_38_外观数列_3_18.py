class Solution:
    def MySloution(self, n):
        if n == 1:
            return '11'
        str1 = str(n)
        length = len(str1)
        print(n, length)
        if length >=1:
            pre = str1[0]
        result = str()
        i = 1
        count = 1
        while i < length: 
            if str1[i] == pre:
                count += 1
            else:
                result += (str(count) + pre)
                pre = str1[i]
                count = 1
            i += 1
        result += (str(count) + pre)
        return result

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        i = 2
        result = self.MySloution(1)
        while i < n:
            result = self.MySloution(result)
            i+=1
        return result

        
