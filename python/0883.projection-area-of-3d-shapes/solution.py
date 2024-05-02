# Created by asetti2002 at 2024/04/25 19:35
# leetgo: 1.4.3
# https://leetcode.com/problems/projection-area-of-3d-shapes/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        return sum(max(row) + max(col) for row in grid for col in zip(*grid) + sum(v != 0 for v in row for row in grid)
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().projectionArea(grid)
    print("\noutput:", serialize(ans, "integer"))
