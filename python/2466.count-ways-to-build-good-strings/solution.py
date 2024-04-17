# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/count-ways-to-build-good-strings/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    low: int = deserialize("int", read_line())
    high: int = deserialize("int", read_line())
    zero: int = deserialize("int", read_line())
    one: int = deserialize("int", read_line())
    ans = Solution().countGoodStrings(low, high, zero, one)
    print("\noutput:", serialize(ans, "integer"))
