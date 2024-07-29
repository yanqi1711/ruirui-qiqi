class Solution:
    def magicalString(self, n: int) -> int:
        if n < 4:
            return 1
        # 开始模拟 1 2 2
        # 1 代表1 2代表有2个数并且和1不一样 故数字变为 1 2 2
        # 第三个2 代表 1 1(因为2不能和第二组的2相同 不然就是4了)
        def notNumber(m):
           return  2 if m == 1 else 1
        string = [1,2,2]
        result = 1
        i = 2
        n-=3
        while True:
            count = string[i]
            addNum = notNumber(string[-1])
            while count:
                string.append(addNum)
                if n!=0 and addNum == 1:
                    result += 1
                n-=1
                if n  == 0:
                    return result
                count -=1
            i+=1