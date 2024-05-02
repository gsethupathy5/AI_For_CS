# Created by asetti2002 at 2024/05/01 19:59
# leetgo: 1.4.3
# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        
        m, n = len(grid), len(grid[0])
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0] % k == 0
        
        for i in range(1, m):
            dp[i][0] = (dp[i-1][0] * 10 + grid[i][0]) % k == 0
        
        for j in range(1, n):
            dp[0][j] = (dp[0][j-1] * 10 + grid[0][j]) % k == 0
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = (dp[i-1][j] * 10 + grid[i][j]) % k == 0 or (dp[i][j-1] * 10 + grid[i][j]) % k == 0
                
        return dp[-1][-1] % MOD
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numberOfPaths(grid, k)
    print("\noutput:", serialize(ans, "integer"))
