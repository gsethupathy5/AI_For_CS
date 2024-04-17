# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/rectangle-area/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    ax1: int = deserialize("int", read_line())
    ay1: int = deserialize("int", read_line())
    ax2: int = deserialize("int", read_line())
    ay2: int = deserialize("int", read_line())
    bx1: int = deserialize("int", read_line())
    by1: int = deserialize("int", read_line())
    bx2: int = deserialize("int", read_line())
    by2: int = deserialize("int", read_line())
    ans = Solution().computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
    print("\noutput:", serialize(ans, "integer"))
