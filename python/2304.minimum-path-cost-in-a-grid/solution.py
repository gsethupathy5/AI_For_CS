# Created by asetti2002 at 2024/04/25 20:24
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-path-cost-in-a-grid/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = grid[0][:]
        
        for i in range(1, m):
            new_dp = [float('inf')] * n
            for j in range(n):
                for k in range(n):
                    new_dp[k] = min(new_dp[k], dp[j] + moveCost[grid[j]][k])
            dp = new_dp
        
        return min(dp)
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    moveCost: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minPathCost(grid, moveCost)
    print("\noutput:", serialize(ans, "integer"))
