# Created by asetti2002 at 2024/04/25 20:06
# leetgo: 1.4.3
# https://leetcode.com/problems/largest-1-bordered-square/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
            row, col = len(grid), len(grid[0])
            m = min(row, col)
            dp = [[[0]*2 for _ in range(col)] for _ in range(row)]
            res = 0
            for i in range(row):
                for j in range(col):
                    if grid[i][j] == 1:
                        dp[i][j][0] = 1 if j == 0 else dp[i][j-1][0] + 1
                        dp[i][j][1] = 1 if i == 0 else dp[i-1][j][1] + 1
            for i in range(row):
                for j in range(col):
                    for k in range(m-1, -1, -1):
                        if i - k >= 0 and j - k >= 0:
                            if min(dp[i][j][0], dp[i][j-k][0], dp[i-k][j][1], dp[i][j][1]) >= k:
                                res = max(res, (k + 1)*(k + 1))
                                break
            return res
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().largest1BorderedSquare(grid)
    print("\noutput:", serialize(ans, "integer"))
