# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/get-equal-substrings-within-budget/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    maxCost: int = deserialize("int", read_line())
    ans = Solution().equalSubstring(s, t, maxCost)
    print("\noutput:", serialize(ans, "integer"))
