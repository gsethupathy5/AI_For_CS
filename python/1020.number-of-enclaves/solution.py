# Created by asetti2002 at 2024/04/25 19:55
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-enclaves/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    dfs(i + x, j + y)

        for i in range(len(grid)):
            dfs(i, 0)
            dfs(i, len(grid[0])-1)

        for j in range(len(grid[0])):
            dfs(0, j)
            dfs(len(grid)-1, j)

        return sum(sum(row) for row in grid)
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().numEnclaves(grid)
    print("\noutput:", serialize(ans, "integer"))
