# Created by asetti2002 at 2024/05/01 20:15
# leetgo: 1.4.3
# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        def is_vowel(word):
            vowels = ['a', 'e', 'i', 'o', 'u']
            return word[0] in vowels and word[-1] in vowels

        count = 0
        for i in range(left, right + 1):
            if is_vowel(words[i]):
                count += 1
        
        return count
# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    left: int = deserialize("int", read_line())
    right: int = deserialize("int", read_line())
    ans = Solution().vowelStrings(words, left, right)
    print("\noutput:", serialize(ans, "integer"))
