# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-cost-to-set-cooking-time/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    startAt: int = deserialize("int", read_line())
    moveCost: int = deserialize("int", read_line())
    pushCost: int = deserialize("int", read_line())
    targetSeconds: int = deserialize("int", read_line())
    ans = Solution().minCostSetTime(startAt, moveCost, pushCost, targetSeconds)
    print("\noutput:", serialize(ans, "integer"))
