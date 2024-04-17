# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/robot-bounded-in-circle/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    instructions: str = deserialize("str", read_line())
    ans = Solution().isRobotBounded(instructions)
    print("\noutput:", serialize(ans, "boolean"))
