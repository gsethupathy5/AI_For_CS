# Created by asetti2002 at 2024/04/25 20:23
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-closed-islands/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 0:
                grid[i][j] = 1
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)
        
        for i in range(len(grid)):
            dfs(i, 0)
            dfs(i, len(grid[0]) - 1)
        
        for j in range(len(grid[0])):
            dfs(0, j)
            dfs(len(grid) - 1, j)
        
        count = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 0:
                    count += 1
                    dfs(i, j)
        
        return count
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().closedIsland(grid)
    print("\noutput:", serialize(ans, "integer"))
