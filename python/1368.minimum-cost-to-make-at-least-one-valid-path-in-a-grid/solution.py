# Created by asetti2002 at 2024/04/25 20:35
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        pass  # Your code here
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minCost(grid)
    print("\noutput:", serialize(ans, "integer"))
