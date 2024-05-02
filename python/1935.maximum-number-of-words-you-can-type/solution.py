# Created by asetti2002 at 2024/04/25 20:09
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-words-you-can-type/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        for word in text.split():
            if not any(letter in brokenLetters for letter in word):
                count += 1
        return count
# @lc code=end

if __name__ == "__main__":
    text: str = deserialize("str", read_line())
    brokenLetters: str = deserialize("str", read_line())
    ans = Solution().canBeTypedWords(text, brokenLetters)
    print("\noutput:", serialize(ans, "integer"))
