# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/robot-return-to-origin/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    moves: str = deserialize("str", read_line())
    ans = Solution().judgeCircle(moves)
    print("\noutput:", serialize(ans, "boolean"))
