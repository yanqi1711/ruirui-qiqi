class Solution:
    def reverse_slice(self, s, start, end):
        return s[:start] + s[start:end][::-1] + s[end:]

    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        length = len(s)
        while i < length:
            # 剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
            if i+k <= length:
                s = self.reverse_slice(s, i,i+k)
                i += 2 *k
                continue
            # 剩余字符少于 k 个，则将剩余字符全部反转。
            s = self.reverse_slice(s,i, length)
            i += 2 *k
        return s