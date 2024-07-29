class Solution:
    def solveEquation(self, equation: str) -> str:
        left,right = equation.split("=")[0],equation.split("=")[1]
        length_left,length_right = len(left),len(right)
        i = 0
        left_x,right_x = 0,0
        left_num,right_num = 0,0
        while i < length_left:
            x,sign = 0,1
            j = 0
            if left[i] == "-" or left[i] == "+":
                if left[i] == "-":
                    sign = -1
                j = i+1
                i+=1
            while i < length_left and left[i].isdigit():
                x = x*10 +int(left[i])
                i += 1
            if i < length_left and left[i] == "x":
                if j == i:
                    x = 1
                    left_x += x *sign
                else:
                    x = 0
                    while j < i and left[j].isdigit():
                        x = x*10+int(left[j])
                        j+=1
                    left_x += x *sign
                i+=1
            else:
                left_num += x*sign
        i = 0
        while i < length_right:
            x,sign = 0,1
            j = 0
            if right[i] == "-" or right[i] == "+":
                if right[i] == "-":
                    sign = -1
                j = i+1
                i+=1
            while i < length_right and right[i].isdigit():
                x = x*10 +int(right[i])
                i += 1
            # 针对x得处理 有数字从0开始 没有 默认为1
            if i < length_right and right[i] == "x":
                if j == i:
                    x = 1
                    right_x += x *sign
                else:
                    x = 0
                    while j < i and right[j].isdigit():
                        x = x*10+int(right[j])
                        j+=1
                    right_x += x *sign
                i+=1
            else:
                right_num += x*sign
        print(left_x,left_num,right_x,right_num)
        if left_x - right_x == 0:
            if (right_num - left_num) != 0:
                return "No solution"
            else:
                return "Infinite solutions"
        value = (right_num - left_num) // (left_x - right_x)
        return f"x={value}"