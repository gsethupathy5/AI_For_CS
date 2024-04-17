# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().isPrefixString(s, words)
    print("\noutput:", serialize(ans, "boolean"))
