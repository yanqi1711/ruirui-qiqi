from typing import List
class Solution:
    def compress(self, chars: List[str]):
        length = len(chars)
        if length == 1:
            return 1
        i = 0
        result = 0
        write = 0
        while i < length:
            count = 1
            pre = chars[i]
            while i+1 < length and pre == chars[i+1]:
                count += 1
                i += 1
            i+=1
            if count == 1:
                result += 1
                chars[write] = pre
                write +=1
            else:
                result += 1
                chars[write] = pre
                write +=1
                for j in str(count):
                    chars[write] = j
                    write +=1
                    result += 1
        print(result)
        return result
            