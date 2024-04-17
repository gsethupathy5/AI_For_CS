# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    locked: str = deserialize("str", read_line())
    ans = Solution().canBeValid(s, locked)
    print("\noutput:", serialize(ans, "boolean"))
