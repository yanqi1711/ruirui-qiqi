def build_next(patt):
    ans = [0]
    prefix_len = 0
    i= 1
    while  i< len(patt):
        if patt[i] == patt[prefix_len]:
            prefix_len+=1
            ans.append(prefix_len)
            i+=1
        else:
            if prefix_len == 0:
                ans.append(0)
                i+=1
            else:
                prefix_len = ans[prefix_len-1]
    return ans
def kmp(string, patt)->bool:
    # print(string, " ", patt)
    nextArray = build_next(patt)
    j=0
    lengthNext = len(patt)
    for i in range(len(string)):
        # next 是数组 不是比较对象
        while j >0 and patt[j] != string[i]:
            j = nextArray[j-1]
        if string[i] == patt[j]:
            j+=1
        if j== lengthNext:
            return True
    return False
class Solution:
    # 这一题只用kmp next数组的一部分
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        length = len(s)
        rever_s = s[::-1]
        for i in range(length-1,-1,-1):
            if s[:i+1] == rever_s[length-1-i:]:
                return rever_s[:length-1-i] + s