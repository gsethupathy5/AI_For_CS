# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/regular-expression-matching/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    p: str = deserialize("str", read_line())
    ans = Solution().isMatch(s, p)
    print("\noutput:", serialize(ans, "boolean"))
