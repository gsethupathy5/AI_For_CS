# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    left: int = deserialize("int", read_line())
    right: int = deserialize("int", read_line())
    ans = Solution().vowelStrings(words, left, right)
    print("\noutput:", serialize(ans, "integer"))
