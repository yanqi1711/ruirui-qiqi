singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        def toEnglish(num:int) -> str:
            result = ""
            if num >= 100:
                # 要用英文表示 所以使用 singles
                count = num // 100
                result += (singles[count]+" Hundred ")
                num %= 100
            if num >= 20:
                count = num // 10
                result += tens[count] + " "
                num %= 10 
            if 10 <= num <20:
                result += teens[num - 10] + ' '
            #必须使用elif
            # 50 因为50%10 = 0 所以0过来多加了个0
            elif 0<num < 10:
                result += singles[num] + " "
            return result
        result = ""
        unit = int(1e9)
        # 3 2 1 0 遍历thousands
        for i in range(3,-1,-1):
            # 从十亿开始
            cur = num // unit
            if cur:
                # 减去已经遍历的位
                num -= cur * unit
                result += toEnglish(cur) + thousands[i] + " "
            unit //= 1000
        return result.strip()