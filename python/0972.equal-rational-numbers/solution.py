# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/equal-rational-numbers/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().isRationalEqual(s, t)
    print("\noutput:", serialize(ans, "boolean"))
