class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        s = list(map( lambda x: ''.join(reversed(x)) ,s))
        s = ' '.join(s)
        return s