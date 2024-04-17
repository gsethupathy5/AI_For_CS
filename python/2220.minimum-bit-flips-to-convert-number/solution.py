# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    start: int = deserialize("int", read_line())
    goal: int = deserialize("int", read_line())
    ans = Solution().minBitFlips(start, goal)
    print("\noutput:", serialize(ans, "integer"))
