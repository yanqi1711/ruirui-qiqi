"""
537. 复数乘法
已解答
中等
相关标签
相关企业
复数 可以用字符串表示，遵循 "实部+虚部i" 的形式，并满足下述条件：

实部 是一个整数，取值范围是 [-100, 100]
虚部 也是一个整数，取值范围是 [-100, 100]
i2 == -1
给你两个字符串表示的复数 num1 和 num2 ，请你遵循复数表示形式，返回表示它们乘积的字符串
"""
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1,image1 = int(num1.split('+')[0]),int(num1.split('+')[1][:-1])
        real2,image2 = int(num2.split('+')[0]),int(num2.split('+')[1][:-1])
        resultReal = real1 * real2 + (image1*image2)*(-1)
        resultImage = real1 *image2 + real2 * image1
        return str(resultReal) + "+" + str(resultImage) + "i"