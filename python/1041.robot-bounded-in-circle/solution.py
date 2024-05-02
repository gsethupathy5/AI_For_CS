# Created by asetti2002 at 2024/04/25 19:57
# leetgo: 1.4.3
# https://leetcode.com/problems/robot-bounded-in-circle/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == 'R': dx, dy = dy, -dx
            if i == 'L': dx, dy = -dy, dx
            if i == 'G': x, y = x+dx, y+dy
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)
# @lc code=end

if __name__ == "__main__":
    instructions: str = deserialize("str", read_line())
    ans = Solution().isRobotBounded(instructions)
    print("\noutput:", serialize(ans, "boolean"))
