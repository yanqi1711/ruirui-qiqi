#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param str string字符串 
# @return string字符串
#
class Solution:
    def ReverseSentence(self , str: str) -> str:
        # write code here
        my_list = str.split(' ')
        print(my_list[::-1])
        return ' '.join(my_list[::-1])