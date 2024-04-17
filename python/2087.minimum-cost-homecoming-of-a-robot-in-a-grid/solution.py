# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    startPos: List[int] = deserialize("List[int]", read_line())
    homePos: List[int] = deserialize("List[int]", read_line())
    rowCosts: List[int] = deserialize("List[int]", read_line())
    colCosts: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minCost(startPos, homePos, rowCosts, colCosts)
    print("\noutput:", serialize(ans, "integer"))
