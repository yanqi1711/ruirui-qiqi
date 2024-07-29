class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        n = len(s1)
        # 生成dp数组
        dp = [[[False for _ in range(n+1)] for _ in range(n)] for _ in range(n)]
        # 初始化每次切割次数为1的情况  为1的情况在切割为2的情况用2->(1,1) 3-> (1,2)
        # 在这里内部其实就已经对于是否存在相同的词频 进行了记录 但是不明显
        for i in range(n):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i][j][1] = True
        # 每次分隔len个词 从2开始
        for length in range(2, n+1):
            # 从0开始 但是切割长度唱过n就不合题意
            for i in range(n + 1- length):
                for j in range(n + 1- length):
                    # 对length个词 再次分割 至少为1
                    for k in range(1, length):
                        # 很重要 多写几遍 多理解最后一个 -1维度一定是k和length-k
                        if (dp[i][j][k] and dp[i+k][j+k][length-k]) or (dp[i][j + length-k][k] and dp[i+k][j][length-k]):
                            dp[i][j][length]=True
        return dp[0][0][n]

        # 检测 字符是否相同
        
        # # cache 会把相同的结果存起来 相当于dp
        # @cache
        # def dfs(i1: int, i2: int, length: int) -> bool:
        #     """
        #     第一个字符串从 i1 开始，第二个字符串从 i2 开始，子串的长度为 length，是否和谐
        #     """

        #     # 判断两个子串是否相等
        #     if s1[i1:i1+length] == s2[i2:i2+length]:
        #         return True
            
        #     # 判断是否存在字符 c 在两个子串中出现的次数不同
        #     if Counter(s1[i1:i1+length]) != Counter(s2[i2:i2+length]):
        #         return False
            
        #     # 枚举分割位置
        #     for i in range(1, length):
        #         # 不交换的情况
        #         if dfs(i1, i2, i) and dfs(i1 + i, i2 + i, length - i):
        #             return True
        #         # 交换的情况
        #         if dfs(i1, i2 + length - i, i) and dfs(i1 + i, i2, length - i):
        #             return True
        
        #     return False

        # ans = dfs(0, 0, len(s1))
        # dfs.cache_clear()
        # return ans

        # # 递归
        # # 不相等 直接False
        # if len(s1) != len(s2):
        #     return False
        # if s1 == s2:
        #     return True
        # # 检测 字符是否相同
        # if sorted(s1) != sorted(s2):
        #     return False
        # # 从第一个开始比较  [a bcd b acd]
        # for i in range(1, len(s1)):
        #     # or连接2个情况
        #     if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or\
        #         (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
        #         return True
        # return False
