# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/word-pattern/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    pattern: str = deserialize("str", read_line())
    s: str = deserialize("str", read_line())
    ans = Solution().wordPattern(pattern, s)
    print("\noutput:", serialize(ans, "boolean"))
