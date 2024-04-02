class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # 记录字节数
        # 从0开始 默认为1字节
        num_bytes = 0
        for i in data:
            # 如果为0说明当前时第一个字节
            if num_bytes == 0:
                # 通过移位运算 判断 
                if i >> 5 == 0b110:
                    num_bytes = 1
                elif i>> 4 == 0b1110:
                    num_bytes = 2
                elif i >> 3 == 0b11110:
                    num_bytes = 3
                # 超过7位 直接False
                elif (i >> 7) :
                    return False
            # 之后的字节
            else:
                if i >> 6 != 0b10:
                    return False
                num_bytes -=1
        # 刚好等于0 返回 True
        return num_bytes == 0