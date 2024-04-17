# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    patterns: List[str] = deserialize("List[str]", read_line())
    word: str = deserialize("str", read_line())
    ans = Solution().numOfStrings(patterns, word)
    print("\noutput:", serialize(ans, "integer"))
