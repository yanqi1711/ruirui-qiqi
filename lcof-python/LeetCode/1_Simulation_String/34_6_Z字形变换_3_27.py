class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = [""] * numRows
        # 方向 向下为True 向上为False
        down = False
        # 行数
        rows = 0
        for i in s:
            result[rows] += i
            if rows == numRows-1 or rows == 0: down = not down
            if down:
                rows+=1
            else:
                rows -=1
            
        return "".join(result)
