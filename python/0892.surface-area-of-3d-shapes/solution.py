# Created by asetti2002 at 2024/04/25 19:36
# leetgo: 1.4.3
# https://leetcode.com/problems/surface-area-of-3d-shapes/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        total_area = sum(v * 4 + 2 for row in grid for v in row if v > 0)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j > 0:
                    total_area -= min(grid[i][j], grid[i][j - 1]) * 2
                if i > 0:
                    total_area -= min(grid[i][j], grid[i - 1][j]) * 2
        return total_area
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().surfaceArea(grid)
    print("\noutput:", serialize(ans, "integer"))
