class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(i,j):
            while i<j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        left,right = 0,len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -=1
            else:
                return check(left+1, right) or check(left, right-1)
        return True