# Created by asetti2002 at 2024/04/25 19:57
# leetgo: 1.4.3
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for word in words:
            if all(word.count(char) <= chars.count(char) for char in word):
                res += len(word)
        return res
# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    chars: str = deserialize("str", read_line())
    ans = Solution().countCharacters(words, chars)
    print("\noutput:", serialize(ans, "integer"))
