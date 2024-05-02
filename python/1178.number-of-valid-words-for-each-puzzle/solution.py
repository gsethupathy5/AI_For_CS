# Created by asetti2002 at 2024/04/25 20:10
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        from collections import Counter
        from itertools import combinations
        
        def get_combinations(word):
            result = []
            for i in range(1, len(word) + 1):
                result.extend(map("".join, combinations(word, i)))
            return result
        
        word_map = Counter()
        for word in words:
            key = 0
            for char in word:
                key |= 1 << (ord(char) - ord('a'))
            word_map[key] += 1
        
        result = []
        for puzzle in puzzles:
            key = 0
            for char in puzzle:
                key |= 1 << (ord(char) - ord('a'))
            
            first_char_key = 1 << (ord(puzzle[0]) - ord('a'))
            count = 0
            for subkey in get_combinations(puzzle[1:]):
                count += word_map[key | first_char_key | (1 << (ord(subkey) - ord('a')))]
            
            result.append(count)
        
        return result
# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    puzzles: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findNumOfValidWords(words, puzzles)
    print("\noutput:", serialize(ans, "integer[]"))
