# Created by asetti2002 at 2024/04/25 19:49
# leetgo: 1.4.3
# https://leetcode.com/problems/unique-paths-iii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j, empty):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != -1):
                return 0
            if grid[i][j] == 2:
                return 1 if empty == 1 else 0
            
            grid[i][j] = -1
            count = sum(dfs(i+x, j+y, empty-1) for x, y in directions)
            grid[i][j] = 0
            return count

        start = (0, 0)
        empty = sum(cell != -1 for row in grid for cell in row)
        return dfs(start[0], start[1], empty)
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().uniquePathsIII(grid)
    print("\noutput:", serialize(ans, "integer"))
