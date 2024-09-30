class Solution:
    def minSteps(self, n: int) -> int:
        # 8->6次 
        # 1,c-> A p->AA 2,C->AA p:AAAA 3,c->AAAA P-> AAAAAAAA
        # 分解质因子
        ans = 0
        # 2就是质数 只有质数才必须要 copy一次 然后黏贴(n-1)次 所以 遇到2 5 7都必须是 2次 5次 7次
        i = 2
        while i * i <= n:
            while n % i == 0:
                n //= i
                ans += i
            i += 1
        if n>1:
            ans += n
        return ans