# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-path-cost-in-a-grid/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    moveCost: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minPathCost(grid, moveCost)
    print("\noutput:", serialize(ans, "integer"))
