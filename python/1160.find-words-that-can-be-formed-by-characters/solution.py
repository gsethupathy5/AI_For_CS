# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    chars: str = deserialize("str", read_line())
    ans = Solution().countCharacters(words, chars)
    print("\noutput:", serialize(ans, "integer"))
