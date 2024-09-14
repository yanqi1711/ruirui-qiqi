from typing import List
from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        if not s or not words:
            return res
        
        word_count = len(words)
        word_length = len(words[0])
        total_length = word_count * word_length
        s_length = len(s)

        if s_length < total_length:
            return res

        # Count the occurrences of each word in 'words'
        word_map = defaultdict(int)
        for word in words:
            word_map[word] += 1
        
        # We will iterate through the string with different offsets
        for i in range(word_length):
            left = i
            right = i
            current_map = defaultdict(int)
            count = 0

            while right + word_length <= s_length:
                # Get the current word from the substring
                word = s[right:right + word_length]
                right += word_length

                # If the word is part of the words list
                if word in word_map:
                    current_map[word] += 1
                    count += 1

                        # When there are more occurrences of 'word' than required,
                        # move the left pointer to the right to remove the extra occurrences
                    while current_map[word] > word_map[word]:
                        left_word = s[left:left + word_length]
                        current_map[left_word] -= 1
                        count -= 1
                        left += word_length

                    # If the count matches the number of words, we found a valid start index
                    if count == word_count:
                        res.append(left)
                
                # If the word is not in the words list, move both pointers to skip it
                else:
                    current_map.clear()
                    count = 0
                    left = right

        return res

class Solution:
    # 没上面快
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        res = []
        m, n, ls = len(words), len(words[0]), len(s)
        from collections import defaultdict
        differ = defaultdict(int)
        for word in words:
            differ[word] += 1
        # 从0开始
        for i in range(n):
            if i + m * n > ls:
                break
            left = right = i
            # 每次切割n 每次增加n 模拟438题
            while right <= ls:
                str_n = s[ right : right+n]
                differ[str_n] -= 1
                # 开始移动左边
                while differ[str_n] < 0:
                    differ[s[left:left+n]]+=1
                    left += n
                if ((right - left)/n +1 )== m:
                    res.append(left)
                right+=n
        return res
