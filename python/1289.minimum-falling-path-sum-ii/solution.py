# Created by asetti2002 at 2024/04/25 20:04
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-falling-path-sum-ii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        for i in range(1, n):
            for j in range(m):
                grid[i][j] += min(grid[i-1][max(0, j-1):min(m, j+2)])
        
        return min(grid[-1])
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minFallingPathSum(grid)
    print("\noutput:", serialize(ans, "integer"))
