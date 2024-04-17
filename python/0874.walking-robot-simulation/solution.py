# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/walking-robot-simulation/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    commands: List[int] = deserialize("List[int]", read_line())
    obstacles: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().robotSim(commands, obstacles)
    print("\noutput:", serialize(ans, "integer"))
