class Solution:
    def reverseVowels(self, s: str) -> str:
        map = set(['A','E','I','O','U','a','e','i','o','u'])
        left, right = 0,len(s)-1
        s = list(s)
        while left < right:
            if s[left] in map:
                while True:
                    if s[right] in map:
                        s[left], s[right] = s[right], s[left]
                        break
                    else:
                        right -= 1
            elif s[right] in map:
                while True:
                    if s[left] in map:
                        s[left], s[right] = s[right], s[left]
                        break
                    else:
                        left += 1
            left += 1
            right -= 1
        return ''.join(s)

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('AEIOUaeiou')  # 定义元音集合
        left, right = 0, len(s) - 1  # 设置左右指针
        # 将字符串转为列表以便进行修改
        s_list = list(s)
        while left < right:
            # 寻找左侧的元音
            while left < right and s_list[left] not in vowels:
                left += 1
            
            # 寻找右侧的元音
            while left < right and s_list[right] not in vowels:
                right -= 1
            
            # 交换元音
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        
        return ''.join(s_list)  # 将列表重新组合成字符串并返回