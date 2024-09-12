class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_len, t_len = len(s),len(t)
        if s_len < t_len:
            return ''
        from collections import defaultdict
        ds,dt = defaultdict(int),defaultdict(int)
        for char in t:
            dt[char] += 1
        left, cnt = 0,0
        ans = ''
        for right in range(s_len):
            # 1 更新ds
            ds[s[right]] += 1
            # 找到了 就记录 一旦多了 cnt就不能变 因为要记录最短的
            if ds[s[right]] <= dt[s[right]]:
                cnt += 1
            # 2 消除冗余 调整窗口 因为left会移动 所以找的时候不是一直对A或B检查 
            # ABAAAAABC ABC 此时自然而然就会被B卡住
            # 'a' 'b' 卡住 因为left +=1 之后访问这个条件会卡住因为s[1]不存在 string index out of range
            while left <= right and ds[s[left]] > dt[s[left]]:
                ds[s[left]] -= 1
                left += 1
            # 3 更新cnt
            if cnt == t_len:
                if not ans or len(ans) > right - left + 1:
                    ans = s[left:right+1]
        return '' if cnt < t_len else ans



if __name__ == "__main__":
    s = Solution()
    s.minWindow('a','b')