# Created by asetti2002 at 2024/04/25 19:57
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        
        for d in range(2, n):
            for i in range(n - d):
                j = i + d
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + values[i] * values[j] * values[k])
        
        return dp[0][n - 1]
# @lc code=end

if __name__ == "__main__":
    values: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minScoreTriangulation(values)
    print("\noutput:", serialize(ans, "integer"))
