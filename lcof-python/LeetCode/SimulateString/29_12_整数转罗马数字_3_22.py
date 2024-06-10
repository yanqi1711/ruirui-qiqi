class Solution:
    def intToRoman(self, num: int) -> str:
        # 罗马数字 最多三个相同的字母
        # IV IX 为特殊情况
        hashMap = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        result = ""
        for key in hashMap:
            count = num // key
            result += count*hashMap[key]
            num %= key
        return result
