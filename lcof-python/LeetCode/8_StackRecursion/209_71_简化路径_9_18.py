class Solution:
    def simplifyPath(self, path: str) -> str: 
        names = path.split("/")
        ans = []
        for i in names:
            if i == "..":
                # 存在才能弹出
                if ans:
                    ans.pop()
            elif i and i != ".":
                ans.append(i)
        return '/' + '/'.join(ans)