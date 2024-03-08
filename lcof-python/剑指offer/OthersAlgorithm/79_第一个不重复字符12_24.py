class Solution:
    def __init__(self) -> None:
        self.s = ""
        self.mp = {}

    def FirstAppearingOnce(self):
        for c in self.s:
            if self.mp[c] == 1:
                return c      
        return '#'

    def Insert(self, char):
        self.s += char
        if char in self.mp:
            self.mp[char] += 1
        else:
            self.mp[char] = 1