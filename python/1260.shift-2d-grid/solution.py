# Created by asetti2002 at 2024/04/25 20:24
# leetgo: 1.4.3
# https://leetcode.com/problems/shift-2d-grid/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        flattened = [cell for row in grid for cell in row]
        k = k % (m * n)
        flattened = flattened[-k:] + flattened[:-k]
        shifted = [flattened[i*n:(i+1)*n] for i in range(m)]
        return shifted
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().shiftGrid(grid, k)
    print("\noutput:", serialize(ans, "integer[][]"))
