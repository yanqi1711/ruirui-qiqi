class Solution:
    def Permutation(self , str: str) -> List[str]:
        # write code here
        # 1 递归
        # a -> a    [for遍历前面的列表]
        # ab -> a + self.Permutation(b) => ab
        #    -> b + self.Permutation(a) => ba
        # cab -> c + self.Permutation(ab) => cab cba 
        #     -> a + self.Permutation(cb) => acb abc
        #     -> b + self.Permutation(ca) => bca bac
        if len(str) == 1:
            return [str]
        # 哈希 运行速度快一些 list可能运行超时
        lists = set()
        # 开始循环每个字符
        for i in range(len(str)):
            cur = str[i]
            for temp_str in self.Permutation(str[:i]+str[i+1:]):
                # 必须是cur在前
                temp = cur + temp_str
                try:
                    lists.add(temp)
                except:
                    pass
        return list(lists)