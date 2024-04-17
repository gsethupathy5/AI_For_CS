# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/circle-and-rectangle-overlapping/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    radius: int = deserialize("int", read_line())
    xCenter: int = deserialize("int", read_line())
    yCenter: int = deserialize("int", read_line())
    x1: int = deserialize("int", read_line())
    y1: int = deserialize("int", read_line())
    x2: int = deserialize("int", read_line())
    y2: int = deserialize("int", read_line())
    ans = Solution().checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2)
    print("\noutput:", serialize(ans, "boolean"))
