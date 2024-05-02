# Created by asetti2002 at 2024/05/01 19:47
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[1] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j] + dp[i][j-1]) % MOD
                elif i > 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD
                elif j > 0:
                    dp[i][j] = (dp[i][j] + dp[i][j-1]) % MOD
        return dp[-1][-1]
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countPaths(grid)
    print("\noutput:", serialize(ans, "integer"))
