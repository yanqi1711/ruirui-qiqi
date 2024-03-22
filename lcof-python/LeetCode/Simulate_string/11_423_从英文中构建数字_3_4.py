class Solution:
    def originalDigits(self, s: str) -> str:
        array = [0 for _ in range(10)]
        array[0] = s.count("z")      
        array[2] = s.count("w")
        array[4] = s.count("u")
        array[6] = s.count("x")
        array[8] = s.count("g")

        array[3] = s.count("h") - array[8]
        array[5] = s.count("f") - array[4]
        array[7] = s.count("s") - array[6]
        
        array[1] = s.count("o") - array[0] - array[2] - array[4]
        array[9] = s.count("i") - array[5] - array[6] - array[8]
        # 0-10 已经自然排序
        #  str(x) 数字 
        # // array[x] 数字出现的次数
        return "".join(str(x) * array[x] for x in range(10))